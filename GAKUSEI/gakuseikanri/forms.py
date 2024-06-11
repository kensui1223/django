from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id','name','number','email']
        
class StudentSearchForm(forms.Form):
    query = forms.CharField(label='検索', max_length=100, required=False)