from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View, FormView
from django.urls import reverse

from .forms import TaskForm
from .models import Task, Status


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.all()
        context['tasks'] = tasks
        return context


class ViewTemplateView(TemplateView):
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context['task'] = task
        return context

class TaskCreateView(FormView):
    template_name = 'add_new.html'
    form_class = TaskForm

    def form_valid(self, form):
        self.task = Task.objects.create(
            summary=form.cleaned_data['summary'],
            description=form.cleaned_data['description'],
            status=form.cleaned_data['status']
        )
        type_task = form.cleaned_data['type_task']
        self.task.type_task.set(type_task)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.task.pk})


class UpdateTemplateView(FormView):
    template_name = 'edit.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_initial(self):
        initial = {}
        for key in 'summary', 'description', 'status':
            initial[key] = getattr(self.task, key)
        initial['type_task'] = self.task.type_task.all()
        return initial

    def form_valid(self, form):
        self.task.summary = form.cleaned_data['summary']
        self.task.description = form.cleaned_data['description']
        self.task.status = form.cleaned_data['status']
        type_task = form.cleaned_data.pop('type_task')
        self.task.save()
        self.task.type_task.set(type_task)
        # tags = form.cleaned_data.pop('tags')
        # for key, value in form.cleaned_data.items():
        #     if value is not None:
        #         setattr(self.article, key, value)
        # self.article.save()
        # self.article.tags.set(tags)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.task.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)
#
# class UpdateTemplateView(TemplateView):
#     template_name = 'edit.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         pk = self.kwargs.get('pk')
#         task = get_object_or_404(Task, pk=pk)
#         form = TaskForm(initial={
#             "summary": task.summary,
#             "description": task.description,
#             "status": task.status,
#             "type_task": task.type_task})
#         context['task'] = task
#         context['form'] = form
#         return context
#
#     def post(self, request, *args, **kwargs):
#         pk = self.kwargs.get('pk')
#         task = get_object_or_404(Task, pk=pk)
#         form = TaskForm(data=request.POST)
#         if form.is_valid():
#             task.summary = form.cleaned_data['summary']
#             task.description = form.cleaned_data['description']
#             task.status = form.cleaned_data['status']
#             task.type_task = form.cleaned_data['type_task']
#             task.save()
#             return redirect('view', pk=task.pk)
#         else:
#             return self.render_to_response(context={
#                 'task': task,
#                 'form': form
#             })


class DeleteTemplateView(TemplateView):
    template_name = 'delete.html'

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