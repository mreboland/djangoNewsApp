from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # To control the fields listed in Users area under admin login, we use list_display and fieldsets.
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": ("age",)}),
    )
    add_fields = UserAdmin.add_fieldsets + (
        (None, {"fields": ("age",)}),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)
