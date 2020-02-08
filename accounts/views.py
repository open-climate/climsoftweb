from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator

from .forms import LoginForm


@method_decorator(user_passes_test(lambda u: u.is_anonymous, login_url='/', redirect_field_name=None), name='dispatch')
class LoginUser(LoginView):
    pass
    # def get(self, request, *args, **kwargs):
    #     # https://github.com/django/django/blob/master/django/contrib/auth/forms.py#L163
    #     login_form =
    #     context = {
    #         'login_form': login_form,
    #     }
    #     return render(request, 'accounts/login.html', context)
    #
    # def post(self, request, *args, **kwargs):
    #     raise ValueError('here')


class LogoutUser(LogoutView):
    pass
