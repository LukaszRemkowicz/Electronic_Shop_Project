from django.contrib.auth import authenticate



def log_in_form(func):
    def log_wrap(request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
        else:
            return func(request, *args, **kwargs)
    return log_wrap
