from django import forms

class CourseForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.TextInput) # <textarea/>
    price = forms.IntegerField()