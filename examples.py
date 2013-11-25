# -*- coding: utf-8 -*-
from logger import SimpleLogger

# Logger example
config = dict()
config['SIMPLELOGS_URL'] = 'http://192.168.1.102'  # Адрес системы журналирования
config['MODULE_NAME'] = 'elreg'  # Код журналируемой системы для инициализации логера: logging.getLogger(module_name)
config['OWNER'] = dict(name=u'Электронная регистратура', version='2.2.10')  # Owner для системы журналирования
config['DEBUG'] = False  # Флаг, соответствующий debug_mode приложения # write to log all unhandled exceptions if not DEBUG mode

logger = SimpleLogger.get_logger(config.get('SIMPLELOGS_URL'),
                                 config.get('MODULE_NAME'),
                                 config.get('OWNER'),
                                 config.get('DEBUG'))