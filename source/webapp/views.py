from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View

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


class TaskCreateView(View):
    def get(self, request):
        return render(request,'add_new.html', context={'form': TaskForm()})

    def post(self, request):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type_task=form.cleaned_data['type_task']
                )
            return redirect('view', pk=task.pk)
        else:
            return render(request, 'add_new.html', context={
                'form': form,
            })


class UpdateTemplateView(TemplateView):
    template_name = 'edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(initial={
            "summary": task.summary,
            "description": task.description,
            "status": task.status,
            "type_task": task.type_task})
        context['task'] = task
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.type_task = form.cleaned_data['type_task']
            task.save()
            return redirect('view', pk=task.pk)
        else:
            return self.render_to_response(context={
                'task': task,
                'form': form
            })


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