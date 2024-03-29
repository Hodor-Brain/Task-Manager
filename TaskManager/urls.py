"""
URL configuration for TaskManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from TaskManagerApplication import views
from TaskManagerApplication.views import (
    RegistrationView,
    CustomLoginView,
    create_task,
    logout_view,
    main_page,
    TaskDeleteMultipleView, task_update
)

urlpatterns = [
    path('', main_page, name='main-page'),
    path('admin/', admin.site.urls),
    path('tasks/', views.task_list, name='task-list'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('tasks/create/', create_task, name='task-create'),
    path('task/delete-multiple/', TaskDeleteMultipleView.as_view(), name='task-delete-multiple'),
    path('task/update/<int:task_id>/', task_update, name='task-update'),
]
