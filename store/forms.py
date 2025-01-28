from django import forms

class CommandeForm(forms.Form):
    nom = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(max_length=255, required=True)
    ville = forms.CharField(max_length=100, required=True)
    pays = forms.CharField(max_length=100, required=True)
    zipcode = forms.CharField(max_length=10, required=True)
