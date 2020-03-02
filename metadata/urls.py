from django.urls import path

from . import models, forms, views

app_name = 'metadata'


urlpatterns = [
    path('', views.Metadata.as_view(), name='metadata'),
    path('station/', views.MetadataList.as_view(model=models.Station), name='station-index'),
    path('station/select/', name='station-select', view = views.MetadataList.as_view(
        model=models.Station, template_name='metadata/station-select.html', order_by='stationname')),
    path('station/create/', views.MetadataCreate.as_view(model=models.Station), name='station-create'),  # FIXME: defaults to template_name = metadata/station_form.html without model form
    path('station/<pk>/', name='station-read', view=views.MetadataRead.as_view(
        model=models.Station, form_class=forms.StationForm, template_name='metadata/station_form.html'
    )),
    path('station/<pk>/update/', views.MetadataUpdate.as_view(), name='station-update'),
    path('station/<pk>/delete/', views.MetadataDelete.as_view(), name='station-delete'),


    path('element/', views.MetadataList.as_view(model=models.Obselement), name='element-index'),
    path('element/select/', views.MetadataList.as_view(  # returns HTML <option> elements
        model=models.Obselement, template_name='metadata/element-select.html', order_by='elementname'), name='element-select'),
    path('element/create/', views.MetadataCreate.as_view(model=models.Obselement), name='element-create'),  # FIXME: defaults to template_name = metadata/obselement_form.html without model form
    path('element/<pk>/', name='element-read', view=views.MetadataRead.as_view(
        model=models.Obselement, form_class=forms.ElementForm, template_name='metadata/obselement_form.html'
    )),
    path('element/<pk>/update/', views.MetadataUpdate.as_view(model=models.Obselement), name='element-update'),
    path('element/<pk>/delete/', views.MetadataDelete.as_view(model=models.Obselement), name='element-delete'),
]