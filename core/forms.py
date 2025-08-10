from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        labels = {
            'cat':'Category',
            'pub_date':'Announcment Date'
        }

        widgets = {
            'cat':forms.Select(attrs={
                'class':'form-control'
            }),
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'ex. Python ...'
            }),
            'description':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Enter Description',
                'rows':2
            }),
            'level':forms.Select(attrs={
                'class':'form-control',
            }),
            'price':forms.NumberInput(attrs={
                'class':'form-control',
            }),
            'pub_date':forms.DateInput(attrs={
                'class':'form-control',
                'type':'date'
            }),
            'image':forms.FileInput(attrs={
                'class':'form-control'
            })
        }
        