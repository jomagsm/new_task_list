from django.views.generic import TemplateView



class ListView(TemplateView):
    model = None
    context_key = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.get_queryset()
        return context

    def get_queryset(self):
        return self.model.objects.all()