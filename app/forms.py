from django import forms

class PredictionForm(forms.Form):
    header_file = forms.FileField(label='Header File (.hea)')
    data_file = forms.FileField(label='Data File (.dat)')
    notes = forms.CharField(label='Clinical Notes', widget=forms.Textarea)