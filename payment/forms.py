from django import forms
from.models import Khalti

class Khaltiform(forms.ModelForm):
    class Meta:
        model = Khalti
        fields = ['image','Refrence_Code']
