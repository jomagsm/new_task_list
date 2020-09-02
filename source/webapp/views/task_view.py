from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from webapp.views.base_view import SearchView
from webapp.forms import TaskForm, SimpleSearchForm
from webapp.models import Task, Project


class IndexTemplateView(SearchView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    model = Task
    paginate_by = 5
    paginate_orphans = 2
    search_form = SimpleSearchForm


class ViewTemplateView(TemplateView):
    template_name = 'task/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        if task.is_deleted:
            raise Http404('Неииеиеие')
        context['task'] = task
        return context


class TaskCreateView(LoginRequiredMixin,FormView):
    template_name = 'task/add_new.html'
    form_class = TaskForm

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.task.pk})


class UpdateTemplateView(LoginRequiredMixin,UpdateView):
    template_name = 'task/edit.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('view_task', kwargs={'pk': self.object.pk})


class DeleteTemplateView(LoginRequiredMixin,DeleteView):
    template_name = 'task/delete.html'
    model = Task

    # def get_success_url(self):
    #     return reverse('view', kwargs={'pk': self.object.project_pk.pk})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()
        return redirect('view', pk=self.object.project_pk.pk)

def multi_delete(request):
    data= request.POST.getlist('id')
    Task.objects.filter(pk__in=data).delete()
    return redirect('index')


class ProjectTaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'task/add_new.html'
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project_pk = project
        task.save()
        return redirect('view', pk=project.pk)



# class ProjectTaskCreateView(CreateView):
#     model = Task
#     template_name = 'task/add_new.html'
#     form_class = TaskForm
#     print('PFOTKKKKKKKDSFKLSJDGFKLSJDGL')
#
#     def form_valid(self, form):
#         project = get_object_or_404(Task, pk=self.kwargs.get('pk'))
#         task = form.save(commit=False)
#         task.project_pk = project
#         task.save()
#         return redirect('view_task', pk=task.pk)