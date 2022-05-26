from django import forms
from durationwidget.widgets import TimeDurationWidget


gender_choices = [('1', 'man'),('2', 'women'),('3', 'it')]

class MyForms(forms.Form):
    name = forms.CharField(label='User name', initial='User name', error_messages={
        'required': 'Please enter your name'})
    profile_picture = forms.ImageField(widget=forms.FileInput)
    additioal_file = forms.FileField(widget=forms.FileInput)
    email = forms.EmailField(error_messages={'required': 'Please enter your available email'})
    password = forms.CharField(max_length= 20, min_length= 10, widget=forms.PasswordInput())
    age = forms.IntegerField(required=False, help_text='Enter your current age', initial='45')
    agreement = forms.BooleanField(required=False)
    average_score = forms.FloatField(initial=0.1, disabled=True)
    birthday = forms.DateField(widget=forms.SelectDateWidget, required=False)
    work_experience = forms.DurationField(widget=TimeDurationWidget(show_seconds=False, show_minutes=False))
    gender = forms.ChoiceField(choices= gender_choices)
    
    