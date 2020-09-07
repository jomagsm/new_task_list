"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView
from webapp.views import IndexView, ProjectView, ProjectCreate, ProjectUpdateView, ProjectDeleteView
from webapp.views.task_view import IndexTemplateView, ViewTemplateView, TaskCreateView, UpdateTemplateView, DeleteTemplateView, \
    multi_delete, ProjectTaskCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('webapp.urls'))

    # path('admin/', admin.site.urls),
    # path('', IndexView.as_view(), name='index_project'),
    # # path('', IndexTemplateView.as_view(), name='index'),
    # path('project_add',ProjectCreate.as_view(),name='create_project'),
    # path('view_task/<int:pk>/', ViewTemplateView.as_view(), name='view_task'),
    # path('view/<int:pk>/', ProjectView.as_view(),name='view'),
    # path('view/<int:pk>/task/add', ProjectTaskCreateView.as_view(), name='add_task'),
    # # path('add_task', TaskCreateView.as_view(), name='add_task'),
    # path('update_project/<int:pk>',ProjectUpdateView.as_view(),name='update_project'),
    # path('update_task/<int:pk>', UpdateTemplateView.as_view(), name='update_task'),
    # path('delete_project/<int:pk>', ProjectDeleteView.as_view(), name='delete_project'),
    # path('delete_task/<int:pk>', DeleteTemplateView.as_view(), name='delete_task'),
    # path('multi_delete/', multi_delete, name='multi_delete'),
    #
    # path('accounts/login', LoginView.as_view(), name='login'),
    # path('accounts/logout/', LogoutView.as_view(), name='logout')
]
