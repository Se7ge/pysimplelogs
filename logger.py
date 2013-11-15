# -*- coding: utf-8 -*-

import logging
import urllib2
import socket
from pysimplelogs import Simplelog


class SimplelogHandler(logging.Handler):

    def __init__(self, url, module_name):
        logging.Handler.__init__(self)
        self.url = url
        self.module_name = module_name

    def emit(self, record):
        message = self.format(record)
        client = Simplelog(self.url)
        level = logging.getLevelName(self.level).lower()
        if not hasattr(client, level):
            level = 'debug'
        getattr(client, level)(self.module_name, message, [self.module_name])


class SimpleLogger(object):

    @classmethod
    def __check_url(cls, url):
        try:
            if urllib2.urlopen(url, timeout=2).getcode() == 200:
                return True
        except urllib2.URLError, e:
            print u'Проблема с подключением к системе журналирования ({0})'.format(e)
        except socket.timeout, e:
            print u'Проблема с подключением к системе журналирования ({0})'.format(e)
        return False

    @classmethod
    def __log_except(cls, _logger, debug_mode=False):
        #TODO: Нужно ли?! не будет ли зацикливания?
        if not debug_mode:
            # write to log all unhandled exceptions if not DEBUG mode
            import sys
            import traceback

            def log_except_hook(*exc_info):
                text = "".join(traceback.format_exception(*exc_info))
                _logger.error("Unhandled exception: %s", text)

            sys.excepthook = log_except_hook

    @classmethod
    def get_logger(cls, url, module_name, debug_mode=False):
        _logger = logging.getLogger(module_name)
        _logger.setLevel(logging.DEBUG)

        if cls.__check_url(url):
            # create handler
            handler = SimplelogHandler(url, module_name)
            # create formatter
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        else:
            # create handler and set level to debug
            handler = logging.StreamHandler()
            # create formatter
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # set handler level to debug
        handler.setLevel(logging.DEBUG)
        # add formatter to handler
        handler.setFormatter(formatter)

        _logger.addHandler(handler)

        cls.__log_except(_logger, debug_mode)

        return _logger