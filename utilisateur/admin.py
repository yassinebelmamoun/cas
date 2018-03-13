from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from main.models import User as MyUser
from django import forms


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('courtier', 'role',)}),
    )

admin.site.register(MyUser, MyUserAdmin)
