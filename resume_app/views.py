from .models import Education, Experience, Project, Personal, Skill
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
from .forms import UserForm, EducationForm, ExperienceForm, ProjectForm, PersonalForm, SkillForm


def skill_by_category(request):
    skill_list = Skill.objects.filter(user=request.user)
    categories = [skill.category for skill in skill_list]
    skill_groups = {}
    for category in categories:
        skill_groups[category] = [skill for skill in skill_list if skill.category == category]
    return skill_groups

def create_context(request):
    education_list = Education.objects.filter(user=request.user)
    experience_list = Experience.objects.filter(user=request.user)
    project_list = Project.objects.filter(user=request.user)
    personal = Personal.objects.get(user=request.user)
    skill_list = Skill.objects.filter(user=request.user).order_by('category')

    skill_groups = skill_by_category(request)

    education_form = EducationForm(None)
    experience_form = ExperienceForm(None)
    project_form = ProjectForm(None)
    skill_form = SkillForm(None)

    personal_initial_data = {
        'name': personal.name,
        'title': personal.title,
        'job_title': personal.job_title,
        'email': personal.email,
        'location': personal.location,
        'summary': personal.summary,
        'phone': personal.phone,
        'website': personal.website,
        'linkedin': personal.linkedin,
        'github': personal.github
    }
    personal_form = PersonalForm(initial=personal_initial_data)

    education_forms = {}
    for education in education_list:
        data = {'subject': education.subject,
                'institution': education.institution,
                'level': education.level,
                'city': education.city,
                'state': education.state,
                'country': education.country,
                'start_date': education.start_date,
                'end_date': education.end_date,
                'GPA': education.GPA
                }
        education_forms[education.id] = EducationForm(initial=data)

    experience_forms = {}
    for experience in experience_list:
        data = {'job_title': experience.job_title,
                'company': experience.company,
                'description': experience.description,
                'city': experience.city,
                'state': experience.state,
                'country': experience.country,
                'start_date': experience.start_date,
                'end_date': experience.end_date
                }
        experience_forms[experience.id] = ExperienceForm(initial=data)

    project_forms = {}
    for project in project_list:
        data = {'title': project.title,
                'description': project.description,
                'link': project.link,
                'github_link': project.github_link,
                'start_date': experience.start_date,
                'end_date': experience.end_date
                }
        project_forms[project.id] = ProjectForm(initial=data)

    context = {'education_list': education_list,
               'experience_list': experience_list,
               'project_list': project_list,
               'name': request.user.first_name,
               'education_form': education_form,
               'education_forms': education_forms,

               'experience_form': experience_form,
               'experience_forms': experience_forms,

               'project_form': project_form,
               'project_forms': project_forms,

               'personal_form': personal_form,
               'personal': personal,

               'skills': skill_list,
               'skill_form': skill_form,
               'skill_groups': skill_groups,
               }
    return context

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context = create_context(request)
                return render(request, 'resume_app/index.html', context)
            else:
                return render(request, 'resume_app/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'resume_app/login.html', {'error_message': 'Invalid login'})
    return render(request, 'resume_app/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form
    }
    return render(request, 'resume_app/login.html', context)

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user.set_password(password)
        user.save()

        personal = Personal()
        personal.user = user
        personal.name = username
        personal.email = email
        personal.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context = create_context(request)
                return render(request, 'resume_app/index.html', context)
    context = {
        "form": form,
    }
    return render(request, 'resume_app/registration_form.html', context)

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'resume_app/login.html')
    else:
        context = create_context(request)
    return render(request, 'resume_app/index.html', context)

# Education functions:

def education_create(request):
    if not request.user.is_authenticated():
        return render(request, 'resume_app/login.html')
    else:
        form = EducationForm(request.POST or None)

        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()

            context = create_context(request)
            return render(request, 'resume_app/index.html', context)

        context = create_context(request)
        return render(request, 'resume_app/index.html', context)

class EducationUpdate(UpdateView):
    model = Education
    fields = ['subject', 'institution', 'level', 'city', 'state', 'country', 'start_date', 'end_date', 'GPA']
    template_name_suffix = '_update_form'
    required_css_class = 'required'

def delete_education(request, education_id):
    education = Education.objects.get(pk=education_id)
    education.delete()

    context = create_context(request)
    return render(request, 'resume_app/index.html', context)

# Experience functions

def experience_create(request):
    if not request.user.is_authenticated():
        return render(request, 'resume_app/login.html')
    else:
        form = ExperienceForm(request.POST or None)

        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()

            context = create_context(request)
            return render(request, 'resume_app/index.html', context)

        context = {
            "experience_form": form,
        }
        return render(request, 'resume_app/experience_form.html', context)

class ExperienceUpdate(UpdateView):
    model = Experience
    fields = ['job_title', 'company', 'description', 'city', 'state', 'country', 'start_date', 'end_date']
    template_name_suffix = '_update_form'

def delete_experience(request, experience_id):
    experience = Experience.objects.get(pk=experience_id)
    experience.delete()

    context = create_context(request)
    return render(request, 'resume_app/index.html', context)


# Project functions

def project_create(request):
    if not request.user.is_authenticated():
        return render(request, 'resume_app/login.html')
    else:
        form = ProjectForm(request.POST or None)

        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()

            context = create_context(request)
            return render(request, 'resume_app/index.html', context)

        context = {
            "project_form": form,
        }
        return render(request, 'resume_app/project_form.html', context)

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['title', 'description', 'link', 'github_link', 'start_date', 'end_date']
    template_name_suffix = '_update_form'

def delete_project(request, project_id):
    project = Experience.objects.get(pk=project_id)
    project.delete()

    context = create_context(request)
    return render(request, 'resume_app/index.html', context)

class PersonalUpdate(UpdateView):
    model = Personal
    fields = ['name', 'title', 'job_title', 'email', 'location', 'phone', 'website', 'linkedin', 'github']
    template_name_suffix = '_update_form'


# Skill functions

def skill_create(request):
    if not request.user.is_authenticated():
        return render(request, 'resume_app/login.html')
    else:
        form = SkillForm(request.POST or None)

        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()

            context = create_context(request)
            return render(request, 'resume_app/index.html', context)

        context = {
            "skill_form": form,
        }
        return render(request, 'resume_app/skill_form.html', context)


def delete_skill(request, skill_id):
    skill = Skill.objects.get(pk=skill_id)
    skill.delete()

    context = create_context(request)
    return render(request, 'resume_app/index.html', context)


def generate_resume(request, theme_id):
    if not request.user.is_authenticated():
        return render(request, 'resume_app/login.html')
    else:
        context = create_context(request)
    return render(request, 'resume_app/themes/theme%s.html' % theme_id, context)
