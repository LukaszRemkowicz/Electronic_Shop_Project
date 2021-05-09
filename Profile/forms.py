from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("User with that name already exist")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Acount with that Email already exist")
       

    class Meta:
        model = User

        fields = UserCreationForm.Meta.fields + ('username', 'password1', 'password2', 'email')

        


class AcceptTerms(forms.Form):
    accepted_terms = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'type': 'checkbox',
                                                                                         'class': 'checkbox'}))
