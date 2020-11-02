from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class SignUpForm(UserCreationForm):
    # no need to add the email field here, because I changed the user model - added email field there
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
    # we added this line to override the default form (which only takes username) - now it takes email or username
