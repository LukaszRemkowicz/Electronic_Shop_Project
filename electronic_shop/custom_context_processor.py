from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.utils.deprecation import MiddlewareMixin

from Profile.forms import CustomLoginForm, KeepMeLoggedIn


def login_form_content(request):
    form = CustomLoginForm()
    keep_me = KeepMeLoggedIn()
    return {'login_form': form, 'keep_me': keep_me}
    
    
    

