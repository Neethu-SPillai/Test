from django import forms
from vehicles.models import Vehicle

class vehicleform(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields='__all__'