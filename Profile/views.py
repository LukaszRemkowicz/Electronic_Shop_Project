from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from django.views import View
from .forms import RegisterForm, AcceptTerms
from django.contrib.auth import login


class UserAccount(View):

    def get(self, request):
        return HttpResponse("<b>Settings</b>")


class Register(FormView):
    template_name = 'profile/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('landing-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        accepted_terms = AcceptTerms
        context['accepted_terms'] = accepted_terms

        return context

    def form_valid(self, form): 
        try:
            # email=form.cleaned_data['email']
            email = User.objects.filter(email=form.cleaned_data['email'])[1]
            messages.error(self.request, "Account registered on that email")

            return redirect('register')


        except:
            user = form.save()
        
            if user is not None:
                login(self.request, user)
                messages.info(self.request, "account created")

            return super(Register, self).form_valid(form)

            

        

    def form_invalid(self, form):
    
        messages.error(self.request, form.errors)

        return super(Register, self).form_invalid(form)




    # form = register
    # accepted_terms = terms
    # content = {'form': form,
    #            'accepted_terms': accepted_terms}
    # template_name = 'profile/register.html'
    #
    # def get(self, request):
    #     form = self.form
    #     accepted_terms = self.accepted_terms
    #     content = self.content
    #     print('dlaczego tutaj')
    #
    #     return render(request, self.template_name, content)
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form(request.POST)
    #     accepted_terms = self.accepted_terms(request.POST)
    #     content = self.content
    #
    #     if form.is_valid():
    #         username = form.data['username']
    #         password = form.data['password1']
    #         password2 = form.data['password2']
    #         email = form.data['email']
    #         try:
    #             user = User.objects.get(email=email)
    #             messages.error(request, "There is user registered with that email")
    #             print('not ok')
    #
    #             try:
    #                 user = User.objects.get(username=username)
    #                 messages.error(request, "There is user registered with that email")
    #                 print('not ok')
    #                 return redirect('home')
    #
    #             except ObjectDoesNotExist:
    #                 messages.success(request, "Account created")
    #                 print('not ok')
    #                 return redirect('register')
    #
    #         except ObjectDoesNotExist:
    #             messages.success(request, "Account created")
    #             print('not ok')
    #             return redirect('register')
    #
    #     else:
    #         messages.error(request, form.errors)
    #     return render(request, self.template_name, content)

