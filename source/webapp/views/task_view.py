from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse

from webapp.views.base_view import SearchView
from webapp.forms import TaskForm, SimpleSearchForm
from webapp.models import Task


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
        context['task'] = task
        return context

class TaskCreateView(FormView):
    template_name = 'task/add_new.html'
    form_class = TaskForm

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.task.pk})


class UpdateTemplateView(FormView):
    template_name = 'task/edit.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('initial')
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.task.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)


class DeleteTemplateView(TemplateView):
    template_name = 'task/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context['task'] = task
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')

def multi_delete(request):
    data= request.POST.getlist('id')
    Task.objects.filter(pk__in=data).delete()
    return redirect('index')