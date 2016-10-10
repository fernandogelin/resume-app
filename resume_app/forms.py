from django.contrib.auth.models import User
from django import forms
from .models import Education, Experience, Project

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput({ "placeholder": "password"}))
    username = forms.CharField(widget=forms.TextInput({ "placeholder": "username"}))
    email = forms.EmailField(widget=forms.TextInput({ "placeholder": "email"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['field', 'school', 'degree', 'city', 'state', 'country', 'start_date', 'end_date', 'GPA']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'company', 'description', 'city', 'state', 'country', 'start_date', 'end_date']
