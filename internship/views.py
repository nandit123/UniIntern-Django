from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Company, Opening
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.core.mail import send_mail, BadHeaderError
from internship.forms import ContactForm
# def index(request):
#     all_companies = Company.objects.all()
#     context = {'all_companies': all_companies,}
#     return render(request, 'internship/index.html', context)
#
#
# def details(request, company_id):
#     company = get_object_or_404(Company, pk=company_id)
#     return render(request, 'internship/details.html', {'company': company})


class WelcomeView(generic.TemplateView):
    template_name = 'internship/welcome.html'


class IndexView(generic.ListView):
    template_name = 'internship/index.html'
    context_object_name = 'all_companies'

    def get_queryset(self):
        return Company.objects.all()


def HomeView(request):
    return render(request, 'internship/home.html')


class DetailView(generic.DetailView):
    model = Company
    template_name = 'internship/details.html'


class CompanyCreate(CreateView):
    model = Company
    fields = ['name', 'type', 'industry', 'company_logo']


class CompanyUpdate(UpdateView):
    model = Company
    fields = ['name', 'type', 'industry', 'company_logo']


class CompanyDelete(DeleteView):
    model = Company
    success_url = reverse_lazy('internship:index')


class OpeningCreate(CreateView):
    model = Opening
    fields = ['company', 'title', 'positions', 'skills', 'stipend', 'duration', 'description']


def email(request):
    def __init__(self, user):
        self.user = user

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST, request.user)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = request.user.email
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['HR@company.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/thanks/')
    return render(request, "internship/email.html", {'form': form})


def thanks(request):
    return render(request, 'internship/thanks.html')