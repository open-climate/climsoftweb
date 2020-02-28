from django import forms
from .models import Obselement, Station


class ElementForm(forms.ModelForm):
    class Meta:
        model = Obselement
        labels = {
            'elementid': 'ID',
            'abbreviation': 'Abbreviation',
            'elementname': 'Name',
            'description': 'Description',
            'elementscale': 'Scale',
            'upperlimit': 'Upper Limit',
            'lowerlimit': 'Lower Limit',
            'units': 'Unit',
            'elementtype': 'Type',
            'qctotalrequired': 'Total Required',
            'selected': 'Selected',
        }
        fields = labels.keys()


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        labels = {
            'stationid': 'Station Id',
            'stationname': 'Station Name',
            'wmoid': 'WMO Id',
            'icaoid': 'ICAO Id',
            'latitude': 'Latitude',
            'qualifier': 'Qualifier',
            'longitude': 'Longitude',
            'elevation': 'Elevatin',
            'geolocationmethod': 'Geographical Method',
            'geolocationaccuracy': 'Geographical Accuracy',
            'openingdatetime': 'Opening Date',
            'closingdatetime': 'Closing Date',
            'country': 'Country',
            'authority': 'Authority',
            'adminregion': 'Admin Region',
            'drainagebasin': 'Drainage Basin',
            #'wacaselectione': '',
            #'cptselection': '',
            'stationoperational': 'Station Operational',
        }
        fields = labels.keys()