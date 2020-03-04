from django.urls import path

from . import models, forms, views


app_name = 'keyentry'


HOURLY = {
    'model': 'FormHourly',
    'name': 'hourly',
    'reverse': 'keyentry:form_hourly',
    'selector': 'keyentry/selector_hourly.html',
    'title': 'Hourly Data',
}

DAILY2 = {
    'model': 'FormDaily2',
    'name': 'daily2',
    'reverse': 'keyentry:form_daily2',
    'selector': 'keyentry/selector_daily2.html',
    'title': 'Daily data for the whole month',
}

MONTHLY = {
    'model': 'FormMonthly',
    'name': 'monthly',
    'reverse': 'keyentry:form_monthly',
    'selector': 'keyentry/selector_monthly.html',
    'title': 'Monthly Data',
}

SYNOPTIC2RA1 = {
    'model': 'FormSynoptic2Ra1',
    'name': 'synoptic2ra1',
    'reverse': 'keyentry:form_synoptic2ra1',
    'selector': 'keyentry/selector_synoptic2ra1.html',
    'title': 'Synoptic data for input into TCDF form for RA1',
}


urlpatterns = [
    path('', views.ContentsView.as_view(), name='contents'),
    path('hourly/', views.KeyEntryView.as_view(extra_context=HOURLY), name='form_hourly'),
    path('daily2/', views.KeyEntryView.as_view(extra_context=DAILY2), name='form_daily2'),
    path('monthly/', views.KeyEntryView.as_view(extra_context=MONTHLY), name='form_monthly'),
    path('synoptic2ra1/', views.KeyEntryView.as_view(extra_context=SYNOPTIC2RA1), name='form_synoptic2ra1'),

    path('hourly/<pk>/update/', name='hourly-update', view=views.KeyEntryUpdate.as_view(
        model=models.FormHourly, form_class=forms.HourlyForm, template_name='keyentry/formhourly_form.html')),
    path('daily2/<pk>/update/', name='daily2-update', view=views.KeyEntryUpdate.as_view(
        model=models.FormDaily2, form_class=forms.Daily2Form, template_name='keyentry/formdaily2_form.html')),
    path('monthly/<pk>/update/', name='monthly-update', view=views.KeyEntryUpdate.as_view(
        model=models.FormMonthly, form_class=forms.MonthlyForm, template_name='keyentry/formmonthly_form.html')),
    path('synoptic2ra1/<pk>/update/', name='synoptic2ra1-update', view=views.KeyEntryUpdate.as_view(
        model=models.FormSynoptic2Ra1, form_class=forms.Synoptic2Ra1Form, template_name='keyentry/formsynoptic2ra1_form.html')),
]
