from django import forms
from .models import Departments

class departmentForm(forms.ModelForm):
    class Meta: 
        model = Departments 
        fields = ['name','description','phone','email']