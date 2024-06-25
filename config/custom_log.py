log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "basic": {
            "format": "[%(asctime)s] [APPLOG] [%(levelname)s] : %(message)s"
        },
        "basic2": {
            "format": "[%(asctime)s] [AUDLOG] [%(levelname)s] : %(message)s"
        },
        "basic3": {
            "format": "[%(asctime)s] [AUDLOG] [%(levelname)s] : %(message)s"
        },
        "basic4": {
            "format": "[%(asctime)s] [UserCronPositionUpdate] [%(levelname)s] : %(message)s"
        },
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "format": "[%(asctime)s] [APPLOG] [%(levelname)s] : %(message)s"
        },

    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "debug_handler_application_stderr": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when" : "D",
            "interval" : 1,
            "filename":"./logs/app.log",
            "formatter": "basic",
            "level": "DEBUG",
        },
        "info_handler_application_stderr": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when" : "D",
            "interval" : 1,
            "filename":"./logs/app.log",
            "level": "INFO",
            "formatter": "basic",
        },
        "warning_handler_application_stderr": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when" : "D",
            "interval" : 1,
            "filename":"./logs/app.log",
            "level": "WARN",
            "formatter": "basic",

        },
        "error_handler_application_stderr": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when" : "D",
            "interval" : 1,
            "filename":"./logs/app.log",
            "level": "ERROR",
            "formatter": "basic",

        },
        "debug_handler_third_party_stderr": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when" : "D",
            "interval" : 1,
            "filename":"./logs/app.log",
            "formatter": "basic2",
            "level": "DEBUG",
        },
        "info_handler_third_party_stderr": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when" : "D",
            "interval" : 1,
            "filename":"./logs/app.log",
            "level": "INFO",
            "formatter": "basic2",

        },
        "warning_handler_third_party_stderr": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when" : "D",
            "interval" : 1,
            "filename":"./logs/app.log",
            "level": "WARN",
            "formatter": "basic2",

        },
        "error_handler_third_party_stderr": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when" : "D",
            "interval" : 1,
            "filename":"./logs/app.log",
            "level": "ERROR",
            "formatter": "basic2",

        },
        "debug_handler_audit_log_stderr": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when" : "D",
            "interval" : 1,
            "filename":"./logs/app.log",
            "formatter": "basic3",
            "level": "DEBUG",

        },
        "info_handler_audit_stderr": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when" : "D",
            "interval" : 1,
            "filename":"./logs/app.log",
            "level": "INFO",
            "formatter": "basic3",

        },
        "warning_handler_audit_stderr": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when" : "D",
            "interval" : 1,
            "filename":"./logs/app.log",
            "level": "WARN",
            "formatter": "basic3",

        },
        "error_handler_audit_stderr": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when" : "D",
            "interval" : 1,
            "filename":"./logs/app.log",
            "level": "ERROR",
            "formatter": "basic3",

        },

    },
    "loggers": {
        "default": {
            "handlers": [
                "default"
            ],
            "level": "DEBUG"
        },
        "debug_application": {
            "handlers": [
                "debug_handler_application_stderr"
            ],
            "level": "DEBUG"
        },
        "info_application": {
            "handlers": [
                "info_handler_application_stderr"
            ],
            "level": "INFO"
        },
        "warning_application": {
            "handlers": [
                "warning_handler_application_stderr"
            ],
            "level": "WARN"
        },
        "error_application": {
            "handlers": [
                "error_handler_application_stderr"
            ],
            "level": "ERROR"
        },
        "debug_third_party": {
            "handlers": [
                "debug_handler_third_party_stderr"
            ],
            "level": "DEBUG"
        },
        "info_third_party": {
            "handlers": [
                "info_handler_third_party_stderr"
            ],
            "level": "INFO"
        },
        "warning_third_party": {
            "handlers": [
                "warning_handler_third_party_stderr"
            ],
            "level": "WARN"
        },
        "error_third_party": {
            "handlers": [
                "error_handler_third_party_stderr"
            ],
            "level": "ERROR"
        },
        "debug_audit": {
            "handlers": [
                "debug_handler_audit_log_stderr"
            ],
            "level": "DEBUG"
        },
        "info_audit": {
            "handlers": [
                "info_handler_audit_stderr"
            ],
            "level": "INFO"
        },
        "warning_audit": {
            "handlers": [
                "warning_handler_audit_stderr"
            ],
            "level": "WARN"
        },
        "error_audit": {
            "handlers": [
                "error_handler_audit_stderr"
            ],
            "level": "ERROR"
        },

    },
}
