import re

from cloudshell.shell.core.context_utils import get_decrypted_password_by_attribute_name_wrapper
from cloudshell.shell.core.dependency_injection.context_based_logger import get_logger_with_thread_id

DEFAULT_PROMPT = '\].*[>#]\s*$'
ENABLE_PROMPT = '#\s*$'
CONFIG_MODE_PROMPT = '\(config.*\)#\s*$'


def send_default_actions(session):
    """Send default commands to configure/clear session outputs
    :return:
    """

    enter_enable_mode(session=session)
    session.hardware_expect('terminal length 0', ENABLE_PROMPT)


ENTER_CONFIG_MODE_PROMPT_COMMAND = 'configure'
EXIT_CONFIG_MODE_PROMPT_COMMAND = 'exit'
COMMIT_COMMAND = 'commit'
DEFAULT_ACTIONS = send_default_actions
SUPPORTED_OS = ["IP[ -]?OS"]
AUTHENTICATION_ERROR_PATTERN = r'[Ll]ogin\s*[Ii]ncorrect|' + \
                               '[Bb]ad\s*([Pp]assword(s)?|[Ss]ecret(s)?|[Ff]ailed\s*(to)?\s*[Aa]uthenticate'
ERROR_MAP = {'Database.*Lock.*': 'Database locked out, please try again.'}


def enter_enable_mode(session):
    result = session.hardware_expect('', re_string=DEFAULT_PROMPT)
    if not re.search(ENABLE_PROMPT, result):
        session.hardware_expect('enable', re_string=DEFAULT_PROMPT,
                                expect_map={'[Pp]assword': lambda session: session.send_line(
                                    get_decrypted_password_by_attribute_name_wrapper('Enable Password')())})
    result = session.hardware_expect('', re_string=DEFAULT_PROMPT)
    if not re.search(ENABLE_PROMPT, result):
        raise Exception('enter_enable_mode', 'Enable password is incorrect')


GET_LOGGER_FUNCTION = get_logger_with_thread_id
POOL_TIMEOUT = 300
HE_MAX_LOOP_RETRIES = 0
