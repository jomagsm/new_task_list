from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, ProjectView, ProjectCreate, ProjectUpdateView, ProjectDeleteView, TeamUpdate
from webapp.views.task_view import IndexTemplateView, ViewTemplateView, UpdateTemplateView, \
    DeleteTemplateView, \
    multi_delete, ProjectTaskCreateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index_project'),
    path('project_add', ProjectCreate.as_view(), name='create_project'),
    path('view_task/<int:pk>/', ViewTemplateView.as_view(), name='view_task'),
    path('view/<int:pk>/', ProjectView.as_view(), name='view'),
    path('view/<int:pk>/task/add', ProjectTaskCreateView.as_view(), name='add_task'),
    path('update_project/<int:pk>', ProjectUpdateView.as_view(), name='update_project'),
    path('update_task/<int:pk>', UpdateTemplateView.as_view(), name='update_task'),
    path('delete_project/<int:pk>', ProjectDeleteView.as_view(), name='delete_project'),
    path('delete_task/<int:pk>', DeleteTemplateView.as_view(), name='delete_task'),
    path('multi_delete/', multi_delete, name='multi_delete'),
    path('update_team/<int:pk>', TeamUpdate.as_view(), name='update_team')
]