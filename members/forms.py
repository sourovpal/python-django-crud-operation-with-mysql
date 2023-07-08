
from django import forms
from .models import Member
# class RegosterForm(forms.ModelForm):
class RegosterForm(forms.Form):
    
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    
    
    # class Meta:
    #     model = Member
        
    #     fields = [
    #         'name',
    #         'email',
    #         'phone',
    #     ]