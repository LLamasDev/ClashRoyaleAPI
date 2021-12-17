from django import forms

class Buscar(forms.Form):
	buscar = forms.CharField(max_length=12, min_length=4)