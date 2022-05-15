import logging

from allauth.account.forms import (
    SignupForm,
    LoginForm,
    AddEmailForm,
    ChangePasswordForm,
    SetPasswordForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
)
from allauth.socialaccount.forms import DisconnectForm

from django.forms.widgets import CheckboxInput


logger = logging.getLogger('antenna')


class BaseForm:
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class CustomSignUpForm(BaseForm, SignupForm):
    pass


class CustomLoginForm(BaseForm, LoginForm):
    pass


class CustomAddEmailForm(BaseForm, AddEmailForm):
    pass


class CustomChangePasswordForm(BaseForm, ChangePasswordForm):
    pass


class CustomSetPasswordForm(BaseForm, SetPasswordForm):
    pass


class CustomResetPasswordForm(BaseForm, ResetPasswordForm):
    pass


class CustomResetPasswordKeyForm(BaseForm, ResetPasswordKeyForm):
    pass


class CustomDisconnectForm(BaseForm, DisconnectForm):
    pass