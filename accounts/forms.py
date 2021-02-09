from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # We use the Meta class to override the default fields by setting the model to our CustomUser and using the default fields view Meta.fields which includes all default fields. To add our custom age field we simply tack it on at the end and it will display automatically on our future sign up page.
    class Meta(UserCreationForm):
        # Our CustomUser model contains all the fields of the default (username, first_name, last_name, email, password, groups, and more) User model and our additional age field which we set. However the default fields on UserCreationForm is just username, email and password which doesn't include everythin. We will expand on it later.
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)
        

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
