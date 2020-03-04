"""climsoftweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path, include

from accounts.forms import LoginForm
from accounts.views import LoginUser, LogoutUser
from main import views


urlpatterns = [
    #path('admin/', admin.site.urls),

    path('', views.mainmenu, name='mainmenu'),

    path('login/', name='login', view=LoginUser.as_view(
        authentication_form=LoginForm,
        template_name='accounts/login.html',
        # extra_context={'databases': ['inam_climsoftweb_db']},
    )),

    path('logout/', name='logout_user', view=LogoutUser.as_view(
        next_page='/login',
    )),

    # main
    path('user-admin/', views.user_admin, name='user_admin'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('language/', views.language, name='language'),

    # apps
    path('keyentry/', include('keyentry.urls')),
    path('metadata/', include('metadata.urls')),
]
