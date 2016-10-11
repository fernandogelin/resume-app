from django.contrib import admin
from .models import Personal, Education, Experience, Project, Skill

admin.site.register(Personal)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Skill)
