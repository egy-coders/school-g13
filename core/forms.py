from django import forms
from .models import Course, Contact
from django.core.exceptions import ValidationError
from django.utils import timezone

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
                'placeholder':'ex. Python ...',
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
        
    def clean_cat(self):
        cat = self.cleaned_data.get('cat') 
        if not cat:
            raise ValidationError('Category is required!')
        return cat

    def clean_title(self): # requreid | 5 <  len < 50
        title = self.cleaned_data.get('title') 
        if not  5 <= len(title) <= 50:
            raise ValidationError('Title must be between 5 and 50 Charters!')
        return title

    def clean_pub_date(self): # must be date in future
        pub_date = self.cleaned_data.get('pub_date')  # None
        if pub_date and pub_date < timezone.now().date():
            raise ValidationError("Announcement date must be in the futue")
        return pub_date
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError("Price must be greater than or equal0")
        return price
    
    def clean(self):
        cleaned_data = super().clean()
        level = cleaned_data.get('level')
        featured = cleaned_data.get('featured')

        if level == 'advacned' and not featured:
            self.add_error('featured', 'Advanced Courses must be marked as featured')




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'username':'Full Name',
            'message':'Your Message'
        }
        widgets = {
            'username':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Full Name'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'faird@example.com'
            }),
            'message':forms.Textarea(attrs={
                'class':'form-control',
                'rows':4
            }),
        }