from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, FormView

from .forms import RegistrationForm, TaskForm, TaskSelectionForm
from .models import Task, UserProfile


class RegistrationView(CreateView):
    template_name = 'TaskManagerApplication/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data.get("password1"))
        user.save()

        UserProfile.objects.create(user=user, role="user")

        authenticated_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

        login(self.request, authenticated_user)

        return redirect(self.success_url)


class CustomLoginView(LoginView):
    template_name = 'TaskManagerApplication/login.html'


class TaskDeleteMultipleView(FormView):
    form_class = TaskSelectionForm
    template_name = 'TaskManagerApplication/task_list.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        selected_tasks = form.cleaned_data['tasks']
        if selected_tasks:
            Task.objects.filter(pk__in=selected_tasks).delete()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect(self.success_url)


def logout_view(request):
    logout(request)
    return redirect('/')


def main_page(request):
    return render(request, 'TaskManagerApplication/main_page.html')


def navigation_bar(request):
    return render(request, 'TaskManagerApplication/navbar.html')


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    selection_form = TaskSelectionForm()

    context = {
        'tasks': tasks,
        'selection_form': selection_form,
    }
    return render(request, 'TaskManagerApplication/task_list.html', context)


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Set the user to the logged-in user
            task.save()
            return redirect('task-list')  # Update the view name as needed
    else:
        form = TaskForm()

    return render(request, 'TaskManagerApplication/task_create.html', {'form': form})
