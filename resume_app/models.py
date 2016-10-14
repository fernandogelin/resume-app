from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Personal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, blank=True)
    job_title = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, default="")
    summary = models.TextField(max_length=500, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=(('Traditional', 'Traditional'), ('Modern', ('Modern'))),
                            default='Modern')
    subject = models.CharField(max_length=30)
    institution = models.CharField(max_length=50)
    level = models.CharField(max_length=30, choices=(('Associate', 'Associate'), ('BS', 'BS'),
                                       ('BA', 'BA'), ('MS', 'MS'), ('PHD', 'PHD'),
                                       ('online', 'online'), ('specialization', 'specialization'),
                                       ('certificate', 'certificate')), default='HS')
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField(blank=True, default=date.today)
    end_date = models.DateField(blank=True, default=date.today)
    GPA = models.FloatField(blank=True, null=True)


    def __str__(self):
        return "%s, %s" % (self.subject, self.institution)


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

    def __str__(self):
        return "%s, %s" % (self.job_title, self.company)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    start_date = models.DateField(blank=True, default=date.today)
    end_date = models.DateField(blank=True, default=date.today)

    def __str__(self):
        return self.project_title

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=30)
    category = models.CharField(max_length=50, blank=True, null=True, choices=(
                                                        ('programing language', 'programing language'),
                                                        ('software', 'software'), ('web framework', 'web framework'),
                                                        ('operating system', 'operating system'), ('tools', 'tools'),
                                                        ('languages', 'languages'),
                                                        ('project management', 'project management'),
                                                        ('data science', 'data science'), ('database', 'database'),
                                                        ('design', 'design'), ('cloud computing', 'cloud computing'),
                                                        ('security', 'security')))
    def __str__(self):
        return self.skill
