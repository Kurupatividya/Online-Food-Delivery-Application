from django import forms
from .models import MEMBERSHIP

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = MEMBERSHIP
        fields = ("thumbnails","price","qty")
        widgets = {
            'thumbnails':forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'qty': forms.TextInput(attrs={'class': 'form-control'})
        }