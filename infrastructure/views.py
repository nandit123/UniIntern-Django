from django.shortcuts import render
from userprofile.models import StudentProject

# Create your views here.
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from infrastructure.models import Lab
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class IndexView(generic.ListView):
    template_name = 'infrastructure/index.html'
    context_object_name = 'all_labs'

    def get_queryset(self):
        return Lab.objects.all()


class DetailView(generic.DetailView):
    model = Lab
    template_name = 'infrastructure/details.html'


class LabCreate(generic.CreateView):
    model = Lab
    fields = ['name', 'department', 'description', 'lab_logo']


class LabUpdate(generic.UpdateView):
    model = Lab
    fields = ['name', 'department', 'description', 'lab_logo']


class LabDelete(DeleteView):
    model = Lab
    success_url = reverse_lazy('infrastructure:index')

