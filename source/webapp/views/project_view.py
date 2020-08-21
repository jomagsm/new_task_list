from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse

from webapp.forms import TaskForm
from webapp.models import Project, Task


class IndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    paginate_by = 2
    paginate_orphans = 0

    def get_queryset(self):
        data = Project.objects.all()
        if not self.request.GET.get('is_admin', None):
            data = Project.objects.all()

        # http://localhost:8000/?search=ygjkjhg
        # form = SimpleSearchForm(data=self.request.GET)
        # if form.is_valid():
        #     search = form.cleaned_data['search']
        #     if search:
        #         data = data.filter(Q(title__icontains=search) | Q(author__icontains=search))

        return data


class ProjectView(DetailView):
    template_name = 'project/view.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.all()
        project = self.object
        tasks = tasks.filter(project_pk=project.pk)
        context['tasks'] = tasks
        return context


class ProjectCreate(CreateView):
    template_name = 'project/create.html'
    model = Project
    fields = ['name', 'description', 'start_date', 'finish_date']

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.pk})


class ArticleCommentCreateView(CreateView):
    model = Task
    template_name = 'task/add_new.html'
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project_pk = project
        task.save()
        return redirect('view_task', pk=task.pk)

