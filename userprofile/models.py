from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from infrastructure.models import Lab


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    profile_picture = models.FileField()
    skills = models.CharField(max_length=1000, blank=True)

    def get_absolute_url(self):
        return reverse('userprofile:index')

    def __str__(self):
        return self.name


class StudentProject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    project_picture = models.FileField()
    lab = models.ForeignKey(Lab)
    mentor = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('userprofile:index')