from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from django.contrib.auth import login


# class RegisterForm(UserCreationForm):   
#     class Meta:
#         model = User
#         fields = UserCreationForm.Meta.fields + ('username', 'password1', 'password2', 'email')

#     def clean_username(self):
#         username = self.cleaned_data.get("username")
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError("User with that name already exist")
#         return username

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("Acount with that Email already exist")
#         return email
    
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + (
            "username",
            "password1",
            "password2",
            "email",
        )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("User with that name already exist")

        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Acount with that Email already exist")

        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data.get("email")

        if commit:
            user.save()

        return user

class CustomLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        password = self.data.get('password')
        if User.objects.filter(username=username).exists():
            try:
                user = authenticate(username=username, password=password)
            except:
                raise forms.ValidationError("Error")
        else:
            raise forms.ValidationError("Wrong login")
        return username
        

class AcceptTerms(forms.Form):
    accepted_terms = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'type': 'checkbox',
                                                                                         'class': 'checkbox'}))
    
class KeepMeLoggedIn(forms.Form):
    keep_me_logged = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'type': 'checkbox',
                                                                                         'class': 'checkbox'}))
