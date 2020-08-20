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

# class SearchView(ListView):
#     context_object_name = 'objects'
#     model = None
#     template_name = None
#     ordering = None
#     paginate_by = None
#     paginate_orphans = None
#     search_form = None
#
#
#     def get(self, request, *args, **kwargs):
#         self.form = self.get_search_form()
#         self.search_value = self.get_search_value()
#         return super().get(request, *args, **kwargs)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=object_list, **kwargs)
#         context['form'] = self.form
#         if self.search_value:
#             context['query'] = urlencode({'search': self.search_value})
#         return context
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         if self.search_value:
#             query = Q(title__icontains=self.search_value) | Q(author__icontains=self.search_value)
#             queryset = queryset.filter(query)
#         return queryset
#
#     def get_search_form(self):
#         return self.search_form(self.request.GET)
#
#     def get_search_value(self):
#         if self.form.is_valid():
#             return self.form.cleaned_data['search']
#         return None