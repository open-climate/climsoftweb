from django.shortcuts import render
from django.views import View

from .forms import LoginForm


class LoginUser(View):
    def get(self, request, *args, **kwargs):
        # https://github.com/django/django/blob/master/django/contrib/auth/forms.py#L163
        login_form = LoginForm(
            initial={'username': 'example'},
        )
        context = {
            'login_form': login_form,
        }
        return render(request, 'accounts/login.html', context)
