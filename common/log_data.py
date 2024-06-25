import logging

class ApplicationLogger:
    def info(msg):
        return logging.getLogger('info_application').info(msg)

    def error(msg):
        return logging.getLogger('error_application').error(msg)

    def debug(msg):
        return logging.getLogger('debug_application').debug(msg)

    def warn(msg):
        return logging.getLogger('warning_application').warn(msg)


