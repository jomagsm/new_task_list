from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic import TemplateView, ListView



# class ListView(TemplateView):
#     model = None
#     context_key = 'objects'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context[self.context_key] = self.get_queryset()
#         return context
#
#     def get_queryset(self):
#         return self.model.objects.all()


class SearchView(ListView):
    search_form = None

    def get(self, request, *args, **kwargs):
        if self.get_search_form():
            self.form = self.get_search_form()
            self.search_value = self.get_search_value()
        else:
            self.form = None
            self.search_value = None
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_query(self):
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = self.get_query()
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        search = self.search_form
        if search:
            return self.search_form(self.request.GET)
        return None

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None