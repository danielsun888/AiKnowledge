from django.shortcuts import render

# Create your views here.
from datetime import date

from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet
from search.forms import NotesSearchForm

# class MySearchView(SearchView):
#     """My custom search view."""

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         # further filter queryset based on some set of criteria
#         return queryset.filter(pub_date__gte=date(2015, 1, 1))

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         # do something
#         return context
class MySearchView(SearchView):
    
    template_name = 'search/search.html'
    queryset = SearchQuerySet().filter(content='john')
    form_class = NotesSearchForm


