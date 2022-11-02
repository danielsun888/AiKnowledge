from __future__ import absolute_import

from django import forms

from mdeditor.fields import MDTextFormField
from .models import Articles


from django import forms

from .models import Comment
from django import forms


from django.forms import ModelForm


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')

class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)