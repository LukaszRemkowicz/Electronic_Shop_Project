from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User

        fields = UserCreationForm.Meta.fields + ('username', 'password1', 'password2', 'email')


class AcceptTerms(forms.Form):
    accepted_terms = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'type': 'checkbox',
                                                                                         'class': 'checkbox'}))
