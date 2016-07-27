__author__ = 'shms'

import threading
from cloudshell.networking.ericsson.ipos.ericsson_ipos_resource_driver import EricssonIPOSResourceDriver
from cloudshell.shell.core.context import ResourceCommandContext, ResourceContextDetails, \
    ReservationContextDetails

# class DriverCommandExecution(threading.Thread):
#     def __init__(self, driver_instance, command_name, parameters_name_value_map):
#         threading.Thread.__init__(self)
#
#         self._parameters_name_value_map = parameters_name_value_map
#         self._driver_instance = driver_instance
#         self._command_name = command_name
#         # self._cancellation_context = CancellationContext()
#
#     def run(self):
#         self._result = self._driver_instance.invoke_func(self._command_name,
#                                                          self._parameters_name_value_map)
#
#     def set_cancellation_context(self):
#         # self._cancellation_context.is_cancelled = True
#         pass
#
#     def get_result(self):
#         return self._result
#
#
# class DriverWrapper:
#     def __init__(self, obj):
#         self.instance = obj
#
#     def invoke_func(self, command_name, params):
#         func = getattr(self.instance, command_name)
#
#         return func(**params)

tt = EricssonIPOSResourceDriver()

context = ResourceCommandContext()
context.resource = ResourceContextDetails()
context.resource.name = 'er'
context.reservation = ReservationContextDetails()
context.reservation.reservation_id = 'test_id'
context.resource.attributes = {}
context.resource.attributes['User'] = 'test'
context.resource.attributes['Password'] = 'test'
context.resource.attributes['Enable Password'] = 'test'
context.resource.attributes['CLI Connection Type'] = 'Telnet'
context.resource.attributes['SNMP Read Community'] = 'test'
context.resource.attributes['SNMP Version'] = '2'
context.resource.address = '10.126.144.213'

#threading.Thread(target=tt.send_custom_command, args=[context, 'show configuration']).start()
threading.Thread(target=tt.get_inventory, args=[context]).start()
# print 'Finished'
# tt.send_custom_command(context, 'kuku')
# tt.get_inventory(context)