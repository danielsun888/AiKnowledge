from django import forms
from haystack.forms import SearchForm



class NotesSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()
# class searchForm(SearchForm):
#     start_date = forms.DateField(required=False)
#     end_date = forms.DateField(required=False)

#     def search(self):
#         # First, store the SearchQuerySet received from other processing.
#         sqs = super().search()

#         if not self.is_valid():
#             return self.no_query_found()

#         # Check to see if a start_date was chosen.
#         if self.cleaned_data['start_date']:
#             sqs = sqs.filter(pub_date__gte=self.cleaned_data['start_date'])

#         # Check to see if an end_date was chosen.
#         if self.cleaned_data['end_date']:
#             sqs = sqs.filter(pub_date__lte=self.cleaned_data['end_date'])

#         return sqs