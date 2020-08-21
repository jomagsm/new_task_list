from django.views.generic import ListView, DetailView

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