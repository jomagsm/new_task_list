from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from webapp.forms import TaskForm, ProjectForm, TeamForm
from webapp.models import Project, Task


class IndexView(LoginRequiredMixin,ListView):
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
        if self.request.user in self.get_object().team.all():
            context['tasks'] = tasks
        else:
            context['tasks'] = None
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



class ProjectCreate(PermissionRequiredMixin,CreateView):
    template_name = 'project/create.html'
    model = Project
    fields = ['name', 'description', 'start_date', 'finish_date']
    permission_required = 'webapp.add_project'


    def form_valid(self, form):
        # print(self.request.user)
        project = form.save()
        users = get_user_model().objects.all()
        user = users.filter(pk=self.request.user.pk)
        project.team.set(user)
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.pk})



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


class ProjectUpdateView(PermissionRequiredMixin,UpdateView):
    template_name = 'project/update.html'
    form_class = ProjectForm
    model = Project
    permission_required = 'webapp.add_project'

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin,DeleteView):
    template_name = 'project/delete.html'
    model = Project
    success_url = reverse_lazy('webapp:index_project')
    permission_required = 'webapp.add_project'


class TeamUpdate(PermissionRequiredMixin,UpdateView):
    template_name = 'project/update_team.html'
    form_class = TeamForm
    model = Project
    permission_required = 'webapp.change_project_teams'
    # def get(self, request, *args, **kwargs):
    #     project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
    #     if self.request.user in project.team.all():
    #
    #     return
    #     user = self.request.user
    #

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return super().has_permission() and self.request.user in project.team.all()

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.pk})
