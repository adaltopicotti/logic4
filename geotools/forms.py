from django import forms
from .models import Coordinate


class CoordinateForm(forms.ModelForm):
    lat_deg = forms.IntegerField(required=False, widget=forms.TextInput(
        attrs={'class':'form-control'}))
    lat_min = forms.IntegerField(required=False, widget=forms.TextInput(
        attrs={'class':'form-control'}))
    lat_sec = forms.FloatField(required=False, widget=forms.TextInput(
        attrs={'class':'form-control'}))
    lon_deg = forms.IntegerField(required=False, widget=forms.TextInput(
        attrs={'class':'form-control'}))
    lon_min = forms.IntegerField(required=False, widget=forms.TextInput(
        attrs={'class':'form-control'}))
    lon_sec = forms.FloatField(required=False, widget=forms.TextInput(
        attrs={'class':'form-control'}))
    class Meta:
        model = Coordinate
        fields = (
            'lat_deg',
            'lat_min',
            'lat_sec',
            'lon_deg',
            'lon_min',
            'lon_sec',
            )
