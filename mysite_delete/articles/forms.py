from __future__ import absolute_import
from django import forms
from mdeditor.fields import MDTextFormField
from .models import Articles,Comment,Book
from django.forms import ModelForm
from .models import *
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')

class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class BookForm(forms.Form):
	# chapterNumber=Articles.objects.raw('select  "BookName",max("chapterID") as chapterID from articles_articles group by "bookID","BookName" order by "bookID";')
	book_choices=sorted(set(list(Articles.objects.values_list('bookID','BookName').order_by('bookID').distinct())))

	name = forms.ChoiceField(choices=book_choices)
	# verse= forms.IntegerField(label='verse',required=True)
# class ChaperForm(ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name', 'bookID', 'totalChapters']


# from django_select2 import forms as s2forms
# from django_select2.forms import ModelSelect2Widget
# class BookForm(forms.Form):
#     book = forms.ModelChoiceField(
#         queryset=Book.objects.all(),
#         label="Book",
#         widget=ModelSelect2Widget(
#             model=Book,
#             search_fields=['name__icontains'],
#         )
#     )

#     chapter = forms.ModelChoiceField(
#         queryset=Chapters.objects.all(),
#         label="Chapter",
#         widget=ModelSelect2Widget(
#             model=Chapters,
#             # search_fields=['name__icontains'],
#             dependent_fields={'Book_id': 'Book'},
#             max_results=500,
#         )
#     )