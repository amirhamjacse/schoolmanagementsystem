from .models import Student
from django import forms
class StudentsDataForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'roll', 'class_name','regi_no']
        labels = {'regi_no':'Registrations No'}
        widgets = {'student_name':forms.TextInput(attrs={'class':'form-control'}),
        'roll':forms.NumberInput(attrs={'class':'form-control'}),
        'class_name':forms.TextInput(attrs={'class':'form-control'}),
        'regi_no':forms.NumberInput(attrs={'class':'form-control'}),
        
        }
    
