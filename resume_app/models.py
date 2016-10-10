from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

# Create your models here.

class Personal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, blank=True)
    job_title = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.CharField(max_length=30, verbose_name='Field')
    school = models.CharField(max_length=50)
    degree = models.CharField(max_length=30, choices=(('HS', 'High School'), ('AS', 'Associate'), ('BS', 'BS'),
                                       ('BA', 'BA'), ('MS', 'MS'), ('PHD', 'PHD')), default='HS')
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=50, blank=True)
    start_date = models.DateField(blank=True, default=date.today)
    end_date = models.DateField(blank=True, default=date.today)
    GPA = models.FloatField(blank=True)

    def get_absolute_url(self):
        return reverse('resume_app:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s, %s" % (self.field, self.school)


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=30)
    company = models.CharField(max_length=50)
    description = models.TextField(default="")
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=50, blank=True)
    start_date = models.DateField(blank=True, default=date.today)
    end_date = models.DateField(blank=True, default=date.today)

    def get_absolute_url(self):
        return reverse('resume_app:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s, %s" % (self.job_title, self.company)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField(blank=True)
    start_date = models.DateField(blank=True, default=date.today)
    end_date = models.DateField(blank=True, default=date.today)

    def get_absolute_url(self):
        return reverse('resume_app:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.project_title
