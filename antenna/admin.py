from django.contrib import admin
from antenna import models
from antenna import admin_forms


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    form = admin_forms.UserAdminForm