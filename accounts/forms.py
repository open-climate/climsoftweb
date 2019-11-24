from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    # Extend form to also process database choice
    pass
