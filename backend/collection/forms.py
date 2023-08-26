from django import forms

class IncidentForm(forms.Form):
    message = forms.TextField()