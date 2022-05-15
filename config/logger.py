import os
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

logs_dir = os.path.join(BASE_DIR, 'tmp')
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)


LOGGING_SETTINGS = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': ' '.join([
                '[%(levelname)s]',
                '%(asctime)s',
                '%(module)s(%(funcName)s)',
                '%(message)s',
            ])
        },
        'verbose': {
            'format': ' '.join([
                '[%(levelname)s]',
                '%(asctime)s',
                '%(process)d(%(thread)d)',
                '%(module)s(%(funcName)s)',
                '%(message)s',
            ])
        },
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': ' '.join([
                '[%(server_time)s]',
                '%(message)s',
            ])
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose',
        },
        'antenna': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(logs_dir, 'antenna.log'),
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 10,
            'formatter': 'simple',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'antenna': {
            'handlers': ['antenna', 'console'],
            'level': 'DEBUG',
        },
    }
}