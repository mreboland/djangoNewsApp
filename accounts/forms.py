from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # Testing to see how to make email mandatory
    # Pulled from:
    # https://stackoverflow.com/questions/7682804/django-model-forms-setting-a-required-field
    email = forms.EmailField(required=True)
    # We use the Meta class to override the default fields by setting the model to our CustomUser and using the default fields view Meta.fields which includes all default fields. To add our custom age field we simply tack it on at the end and it will display automatically on our future sign up page.
    class Meta(UserCreationForm):
        # Our CustomUser model contains all the fields of the default (username, first_name, last_name, email, password, groups, and more) User model and our additional age field which we set. However the default fields on UserCreationForm is just username, email and password which doesn't include everythin. We will expand on it later.
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ("age",)
        # As mentioned above, we can choose the fields we want to show by doing the below instead:
        # We don't need to specify password here as it's required.
        fields = ("username", "email", "age",)
        

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ("username", "email", "age",)
