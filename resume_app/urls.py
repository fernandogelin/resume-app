from django.conf.urls import url
from . import views

app_name = 'resume_app'

urlpatterns = [

    # General urls

    # /resume
    url(r'^$', views.index, name="index"),

    # registration page
    url(r'^register/$', views.register, name="register"),

    # user login
    url(r'^login_user/$', views.login_user, name="login_user"),

    # user logout
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # Education urls

    # /resume/edu/add
    url(r'^edu/add/$', views.education_create, name="add_education"),

    # /resume/edu/2
    url(r'^edu/(?P<pk>[0-9]+)/$', views.EducationUpdate.as_view(success_url="/resume/"), name="update_education"),

    # /resume/edu/2/delete
    url(r'^edu/(?P<education_id>[0-9]+)/delete_education/$', views.delete_education, name="delete_education"),

    # Experience urls

    # /resume/experience/add
    url(r'^experience/add/$', views.experience_create, name="add_experience"),

    # /resume/edu/2
    url(r'^experience/(?P<pk>[0-9]+)/$', views.ExperienceUpdate.as_view(success_url="/resume/"), name="update_experience"),

    # /resume/edu/2/delete
    url(r'^experience/(?P<experience_id>[0-9]+)/delete_experience/$', views.delete_experience, name="delete_experience"),

]
