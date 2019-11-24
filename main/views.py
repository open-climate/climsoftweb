from django.contrib.auth.decorators import login_required
from django.shortcuts import render


#@login_required
def mainmenu(request):
    return render(request, 'main/mainmenu.html', {})


#@login_required
def keyentry(request):
    return render(request, 'main/keyentry.html', {})
