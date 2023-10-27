from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm
from .models import Task


class RegistrationView(CreateView):
    template_name = 'TaskManagerApplication/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Automatically log the user in after registration
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CustomLoginView(LoginView):
    template_name = 'TaskManagerApplication/login.html'


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'TaskManagerApplication/task_list.html', {'tasks': tasks})

# Create your views here.
