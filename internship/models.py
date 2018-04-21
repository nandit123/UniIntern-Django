from django.db import models
from django.core.urlresolvers import reverse


class Company(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    company_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('internship:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Opening(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    positions = models.IntegerField()
    skills = models.CharField(max_length=500)
    stipend = models.IntegerField()
    duration = models.IntegerField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('internship:details', kwargs={'pk': self.company.id})