from .models import Education, Experience, Project
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
from .forms import UserForm, EducationForm, ExperienceForm


def create_context(request):
    education_list = Education.objects.filter(user=request.user)
    experience_list = Experience.objects.filter(user=request.user)
    project_list = Project.objects.filter(user=request.user)
    education_form = EducationForm(request.POST or None)
    experience_form = ExperienceForm(request.POST or None)

    education_forms = {}
    for education in education_list:
        data = {'field': education.field,
                'school': education.school,
                'degree': education.degree,
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

    context = {'education_list': education_list,
               'experience_list': experience_list,
               'project_list': project_list,
               'name': request.user.first_name,
               'education_form': education_form,
               'education_forms': education_forms,
               'experience_form': experience_form,
               'experience_forms': experience_forms,
               'sections': ['education', 'experience']
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
    fields = ['field', 'school', 'degree', 'city', 'state', 'country', 'start_date', 'end_date', 'GPA']
    template_name_suffix = '_update_form'

def delete_education(request, education_id):
    education = Education.objects.get(pk=education_id)
    education.delete()

    context = create_context(request)
    return render(request, 'resume_app/index.html', context)

#Experience functions
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
