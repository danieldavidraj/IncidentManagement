from django import forms

class IncidentForm(forms.Form):
    message = forms.CharField(max_length=200)