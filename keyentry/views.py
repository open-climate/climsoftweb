from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def keyentry(request):
    return render(request, 'keyentry/keyentry.html', {})


@login_required
def form_hourly(request):
    return render(request, 'keyentry/form_hourly.html', {})


@login_required
def form_daily2(request):
    return render(request, 'keyentry/form_daily2.html', {})


@login_required
def form_monthly(request):
    return render(request, 'keyentry/form_monthly.html', {})
