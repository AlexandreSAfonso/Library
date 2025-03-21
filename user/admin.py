from django.contrib import admin

from .models import User


@admin.register(User)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('user_name', 'user_email', 'user_password')
