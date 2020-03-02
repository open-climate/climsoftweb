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


urlpatterns = [
    path('', views.ContentsView.as_view(), name='contents'),
    path('hourly/', views.KeyEntryView.as_view(extra_context=HOURLY), name='form_hourly'),
    path('daily2/', views.KeyEntryView.as_view(extra_context=DAILY2), name='form_daily2'),
    path('monthly/', views.KeyEntryView.as_view(extra_context=MONTHLY), name='form_monthly'),

    path('hourly/<pk>/update/', name='hourly-update', view=views.KeyEntryUpdate.as_view(
        model=models.FormHourly, form_class=forms.HourlyForm, template_name='keyentry/formhourly_form.html')),
    path('daily2/<pk>/update/', name='daily2-update', view=views.KeyEntryUpdate.as_view(
        model=models.FormDaily2, form_class=forms.Daily2Form, template_name='keyentry/formdaily2_form.html')),
    path('monthly/<pk>/update/', name='monthly-update', view=views.KeyEntryUpdate.as_view(
        model=models.FormMonthly, form_class=forms.MonthlyForm, template_name='keyentry/formmonthly_form.html')),
]


# path('station/', views.MetadataList.as_view(model=models.Station), name='station-index'),
# path('station/select/', name='station-select', view=views.MetadataList.as_view(
#     model=models.Station, template_name='metadata/station-select.html', order_by='stationname')),
# path('station/create/', views.MetadataCreate.as_view(model=models.Station),
#      name='station-create'),  # FIXME: defaults to template_name = metadata/station_form.html without model form
# path('station/<pk>/', name='station-read', view=views.MetadataRead.as_view(
#     model=models.Station, form_class=forms.StationForm, template_name='metadata/station_form.html'
# )),
# path('station/<pk>/update/', views.MetadataUpdate.as_view(), name='station-update'),
# path('station/<pk>/delete/', views.MetadataDelete.as_view(), name='station-delete'),
