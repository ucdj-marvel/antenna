import os
from pathlib import Path

from dotenv import load_dotenv
from config.logger import LOGGING_SETTINGS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ENV_FILE = os.path.join(BASE_DIR, 'config', '.env')
if os.path.exists(ENV_FILE):
    load_dotenv(ENV_FILE)

DJANGO_ENV = os.environ.get('DJANGO_ENV', 'development')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', '')
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', 0)))

LOGGING = LOGGING_SETTINGS

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'antenna',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE'),
        'USER': os.environ.get('MYSQL_USER'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        'HOST': os.environ.get('MYSQL_HOST'),
        'PORT': '3306'
    }
}


AUTH_USER_MODEL = 'antenna.User'

LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'antenna:index'
ACCOUNT_SIGNUP_REDIRECT_URL = 'account_email_verification_sent'
ACCOUNT_LOGOUT_REDIRECT_URL = 'antenna:index'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# ログイン時の認証方法はemailとパスワードとする
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# 登録時にユーザー名(ユーザーID)必須
ACCOUNT_USERNAME_REQUIRED = True
# ユーザー登録時に入力したメールアドレスに、確認メールを送信する事を必須(mandatory)とする
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ユーザー登録画面でメールアドレス入力を要求する(True)
ACCOUNT_EMAIL_REQUIRED = True
# 登録できるメールアドレスの上限。1だと変更できない。
ACCOUNT_MAX_EMAIL_ADDRESSES = 2
# ログイン試行の許容回数
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3
# 3回ログインに失敗すると、3時間ログインできないようにする
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 10800

# ユーザーネームの最小許容数
ACCOUNT_USERNAME_MIN_LENGTH = 4
# usernameとして使えない文字
ACCOUNT_USERNAME_BLACKLIST = [
    'admin',
    'manko', 'mankko', 'chinko', 'chinkko', 'chinchin',
]
# 確認メールの有効期限
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1

EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'

if DJANGO_ENV == 'production':
    SENDGRID_SANDBOX_MODE_IN_DEBUG = False
else:
    SENDGRID_SANDBOX_MODE_IN_DEBUG = True
    # URLのトラッキングをOFF
    SENDGRID_TRACK_CLICKS_PLAIN = False
    # ターミナルに表示
    SENDGRID_ECHO_TO_STDOUT = True

ACCOUNT_FORMS = {
    'signup' : 'antenna.forms.CustomSignUpForm',
    'login' : 'antenna.forms.CustomLoginForm',
    'add_email': 'antenna.forms.CustomAddEmailForm',
    'change_password': 'antenna.forms.CustomChangePasswordForm',
    'set_password': 'antenna.forms.CustomSetPasswordForm',
    'reset_password': 'antenna.forms.CustomResetPasswordForm',
    'reset_password_from_key': 'antenna.forms.CustomResetPasswordKeyForm',
    'disconnect': 'antenna.forms.CustomDisconnectForm',
}

# ACCOUNT_ADAPTER = 'antenna.adapter.AccountAdapter'


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'antenna', 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
