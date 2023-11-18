from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Task

DUE_DATE_SMALLEST_YEAR = 2020
DUE_DATE_BIGGEST_YEAR = 2039
STATUS_CHOICES = (
    ('todo', 'To Do'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
)


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(DUE_DATE_SMALLEST_YEAR, DUE_DATE_BIGGEST_YEAR + 1))
    )
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    description = forms.CharField(widget=forms.Textarea(attrs={'maxlength': 1000}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control description'


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class TaskSelectionForm(forms.Form):
    tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
