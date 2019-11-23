from django.shortcuts import render

def mainmenu(request):
    return render(request, 'main/mainmenu.html', {})
