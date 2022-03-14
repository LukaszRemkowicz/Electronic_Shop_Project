from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from Profile.forms import CustomLoginForm


class LoginFormMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        login_form = CustomLoginForm()
        login_form_context = {"login_form": login_form}
        request.login_form_context = login_form_context

        response = self.get_response(request)

        if request.method == "POST" in request.POST:

            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
        else:
            pass

        return response

    # def process_view(self, request, view_func, view_args, view_kwargs):

    #     if request.method == 'POST' in request.POST:

    #         form = AuthenticationForm(data=request.POST)
    #         if form.is_valid():

    #             login(request, form.get_user())

    #     else:
    #         form = AuthenticationForm(request)

    #     request.login_form = form
