from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from webapp.forms import TaskForm, ProjectForm
from webapp.models import Project, Task


class IndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    paginate_by = 5
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


# class ProjectView(DetailView):
#     template_name = 'project/view.html'
#     model = Project
#     paginate_by = 5
#     paginate_orphans = 2
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         tasks = Task.objects.all()
#         project = self.object
#         tasks = tasks.filter(project_pk=project.pk, is_deleted=False)
#         context['tasks'] = tasks
#         return context


class ProjectView(DetailView):
    template_name = 'project/view.html'
    model = Project
    paginate_by = 5
    paginate_orphans = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks, page, is_paginated = self.paginate_tasks(self.object)
        # tasks = Task.objects.all()
        # project = self.object
        # tasks = tasks.filter(project_pk=project.pk)
        context['tasks'] = tasks
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        return context

    def paginate_tasks(self, project):
        tasks = project.project.all().filter(is_deleted=False)
        if tasks.count() > 0:
            paginator = Paginator(tasks, self.paginate_by, orphans=self.paginate_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1  # page.has_other_pages()
            return page.object_list, page, is_paginated
        else:
            return tasks, None, False



class ProjectCreate(CreateView):
    template_name = 'project/create.html'
    model = Project
    fields = ['name', 'description', 'start_date', 'finish_date']

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.pk})



# class ArticleCommentCreateView(CreateView):
#     model = Task
#     template_name = 'task/add_new.html'
#     form_class = TaskForm
#
#     def form_valid(self, form):
#         project = get_object_or_404(Task, pk=self.kwargs.get('pk'))
#         task = form.save(commit=False)
#         task.project_pk = project
#         task.save()
#         return redirect('view_task', pk=task.pk)


#
# class ProjectView(DetailView):
#     template_name = 'project/view.html'
#     model = Project
#     paginate_tasks_by = 2
#     paginate_tasks_orphans = 0
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         tasks, page, is_paginated = self.paginate_tasks(self.object)
#
#         context['tasks'] = tasks
#         context['page_obj'] = page
#         context['is_paginated'] = is_paginated
#         return context
#
#     def paginate_tasks(self, project):
#         tasks = project.tasks.all()
#         if tasks.count() > 0:
#             paginator = Paginator(tasks, self.paginate_tasks_by, orphans=self.paginate_tasks_orphans)
#             page_number = self.request.GET.get('page', 1)
#             page = paginator.get_page(page_number)
#             is_paginated = paginator.num_pages > 1  # page.has_other_pages()
#             return page.object_list, page, is_paginated
#         else:
#             return tasks, None, False
#


class ProjectUpdateView(UpdateView):
    template_name = 'project/update.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'project/delete.html'
    model = Project
    success_url = reverse_lazy('index_project')