from django.contrib.auth.models import User
from django import forms
from .models import Education, Experience, Project, Personal, Skill

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
        fields = ['type', 'subject', 'institution', 'level', 'city', 'state', 'country', 'start_date', 'end_date', 'GPA']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'company', 'description', 'city', 'state', 'country', 'start_date', 'end_date']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link', 'github_link', 'start_date', 'end_date']

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['name', 'title', 'job_title', 'email', 'location', 'summary', 'phone', 'website', 'linkedin', 'github']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill', 'category']