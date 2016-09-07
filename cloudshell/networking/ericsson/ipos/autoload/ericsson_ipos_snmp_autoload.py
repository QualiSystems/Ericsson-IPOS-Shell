import os
import time

import inject

from cloudshell.configuration.cloudshell_cli_binding_keys import CLI_SERVICE
from cloudshell.networking.ericsson.autoload.ericsson_generic_snmp_autoload import EricssonGenericSNMPAutoload
from cloudshell.shell.core.context_utils import get_attribute_by_name


class EricssonIPOSSNMPAutoload(EricssonGenericSNMPAutoload):
    def __init__(self, snmp_handler=None, logger=None, supported_os=None, cli=None, snmp_community=None):
        """Basic init with injected snmp handler and logger

        :param snmp_handler:
        :param logger:
        :return:
        """

        EricssonGenericSNMPAutoload.__init__(self, snmp_handler, logger, supported_os)
        self.port_ethernet_vendor_type_pattern = r'port.*\d+ge|\S+.1.193.218.6.10.251|\S+Port.251'
        self._cli = cli
        self.snmp_view = 'qualiview'
        self.snmp_community = snmp_community
        self._enable_snmp = True
        self._disable_snmp = False
        self.vendor_type_exclusion_pattern = ['port.*mgmt']
        self.interface_mapping_key = 'eriRouterIpBindIfIndex'
        self.interface_mapping_mib = 'ERICSSON-ROUTER-IP-BIND-MIB'
        self.load_mib_list = ['ERICSSON-ROUTER-PRODUCT-MIB']
        if not self.snmp_community:
            self.snmp_community = get_attribute_by_name('SNMP Read Community') or 'qualicommunity'

    def load_ericsson_mib(self):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '', 'mib'))
        self.snmp.update_mib_sources(path)

    @property
    def cli(self):
        if self._cli is None:
            self._cli = inject.instance(CLI_SERVICE)
        return self._cli

    def discover(self):
        try:
            self._enable_snmp = (get_attribute_by_name('Enable SNMP') or 'true').lower() == 'true'
            self._disable_snmp = (get_attribute_by_name('Disable SNMP') or 'false').lower() == 'true'
        except:
            pass

        if self._enable_snmp:
            self.enable_snmp()
        try:
            result = self.get_autoload_details()
        except Exception as e:
            self.logger.error('Autoload failed: {0}'.format(e.message))
            raise Exception('EricssonGenericSNMPAutoload', e.message)
        finally:
            if self._disable_snmp:
                self.disable_snmp()
        return result

    def enable_snmp(self):
        snmp_service_enabled = 'not supported' not in self.cli.send_command('show service | include snmp').lower()
        existing_snmp_server = 'snmp server is not running' not in self.cli.send_command('show snmp server').lower()
        existing_snmp_view = self.snmp_view in self.cli.send_command('show snmp view').lower()
        existing_snmp_community = self.snmp_community in self.cli.send_command('show snmp communities').lower()

        if not snmp_service_enabled:
            self.cli.send_config_command('context local')
            self.cli.send_config_command('service snmp server')
            self.cli.send_config_command('end')

        if not existing_snmp_server:
            self.cli.send_config_command('snmp server enhance ifmib')

        if not existing_snmp_view:
            self.cli.send_config_command('snmp view {0} internet included'.format(self.snmp_view))
            if existing_snmp_community:
                self.cli.send_config_command('no snmp community {0}'.format(self.snmp_community))
                existing_snmp_community = False

        if not existing_snmp_community:
            self.cli.send_config_command('snmp community {0} all-contexts view qualiview read-only'.format(
                self.snmp_community))
        self.cli.commit()

    def disable_snmp(self):
        time.sleep(5)
        self.cli.send_config_command('no snmp community {0}'.format(self.snmp_community))
        self.cli.send_config_command('no snmp view {0}'.format(self.snmp_view))
        self.cli.send_config_command('no snmp server')
        self.cli.send_config_command('context local')
        self.cli.send_config_command('default service snmp server')
        self.cli.send_config_command('end')
