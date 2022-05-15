from dataclasses import fields
from django.forms import ModelForm, PasswordInput

from antenna import models


class UserAdminForm(ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'
        widgets = {
            'password': PasswordInput(),
        }