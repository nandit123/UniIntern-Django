from django.db import models
from django.core.urlresolvers import reverse


class Lab(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    lab_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('infrastructure:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
