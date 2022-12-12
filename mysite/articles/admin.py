from django.contrib import admin
from .models import Articles,Comment,Book,Keyword,Chapters,FavoriteVerse
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.

# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('tallImage','description','last_updated')
#     list_display_links = ( 'tallImage','description')
class textEditorAdmin(admin.ModelAdmin):
   list_display = ["title"]
   formfield_overrides = {
   models.TextField: {'widget': TinyMCE()}
   }
# def apply_discount(modeladmin, request, queryset):
#     for articles in queryset:
#         articles.category = book.price * decimal.Decimal('0.9')
#         articles.save()
# apply_discount.short_description = 'Apply 10%% discount'

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title','book','text',)
    list_display_links = ( 'title','text')
    ordering = ['id']
    exclude = ('manyKeywords',)

    search_fields = ['title','text']

   #  actions = [apply_discount, ]  # <-- Add the list action function here
admin.site.register(Articles,ArticlesAdmin)

# admin.site.register(ArticlesAdmin)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name','frequency',)
    list_display_links = ('name','frequency',)
   #  actions = [apply_discount, ]  # <-- Add the list action function here
admin.site.register(Keyword,KeywordAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'post', 'created', 'active')
	list_filter = ('active', 'created', 'updated')
	search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)

class BookAdmin(admin.ModelAdmin):
   list_display=('name','bookID')
   # ordering = ['bookID']
admin.site.register(Book,BookAdmin)

class FavoriteVerseAdmin(admin.ModelAdmin):
   list_display=('user','verse','comment')
   # ordering = ['name']
admin.site.register(FavoriteVerse,FavoriteVerseAdmin)