from django import forms
from .models import product


class prodForm(forms.ModelForm):
	class Meta:
		model = product
		fields = [
			'title',
			'description',
			'price'
		]

class RawProdForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs = {
			"placeholder" : "come on :)"
		}))
	description =  forms.CharField(required=False, widget=forms.Textarea(attrs = {
			"class" : "newOne",
			"rows" : 5,
			"cols" : 50,
			"placeholder" : "just do it"
			})
		)
	price = forms.DecimalField(initial=0.00)