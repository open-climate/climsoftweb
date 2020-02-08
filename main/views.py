from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def mainmenu(request):
    return render(request, 'main/mainmenu.html', {})


@login_required
def keyentry(request):
    return render(request, 'main/keyentry.html', {})


@login_required
def keyentry_hourly(request):
    return render(request, 'main/keyentry_hourly.html', {})


@login_required
def metadata(request):
    return render(request, 'main/metadata.html', {})


@login_required
def user_admin(request):
    return render(request, 'main/user_admin.html', {})


@login_required
def user_profile(request):
    return render(request, 'main/user_profile.html', {})


@login_required
def change_password(request):
    return render(request, 'main/change_password.html', {})


@login_required
def language(request):
    return render(request, 'main/language.html', {})
