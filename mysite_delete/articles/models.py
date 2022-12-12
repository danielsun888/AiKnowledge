
# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse
# from tinymce.models import HTMLField 
# from mdeditor.fields import MDTextField
import markdown  # 需要pip进行安装
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

# bible books
class Book(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    bookID=models.IntegerField(null=True,blank=True)
    totalChapters = models.IntegerField(null=True, blank=True)
    # slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    # date_created = models.DateTimeField(blank=True, null=True)
    # last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


    # def get_absolute_url(self):
    #     return reverse('category-detail', kwargs={'pk': self.pk})


#     def save(self, *args, **kwargs):
#         if self.date_created is None:
#             self.date_created = timezone.localtime(timezone.now())
#         if self.uniqueId is None:
#             self.uniqueId = str(uuid4()).split('-')[4]
#             self.slug = slugify('{} {}'.format(self.title, self.uniqueId))


#         self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
#         self.last_updated = timezone.localtime(timezone.now())
#         super(Category, self).save(*args, **kwargs)

# bible chapters
class Chapters(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    chapterID=models.IntegerField(null=True,blank=True)
    Book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    bookName = models.CharField(null=True, blank=True, max_length=200)
     
    testament_CHOICES = (
        (u'old', u'old testament'),
        (u'new', u'new testament'),
    )
    testament = models.CharField(max_length=20, choices=testament_CHOICES,default='old')
    # slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    # date_created = models.DateTimeField(blank=True, null=True)
    # last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)
    class Meta:
            ordering = ['id']
class Keyword(models.Model):
    name = models.CharField(_('name'),max_length=500)
    frequency = models.BigIntegerField(_('frequency'),)
    def __str__(self):
        return '{}'.format(self.name)
# bible verses
class Articles(models.Model):
    title = models.TextField(_('title'),null=True,blank=True)
    # # desc = models.TextField(null=True)
    # photo = models.ImageField(null=True,blank=True,upload_to='photos')
    # file = models.FileField(null=True,blank=True,upload_to ='files/% Y/% m/% d/')
    bookID=models.BigIntegerField(null=True,blank=True)
    chapterID=models.BigIntegerField(null=True,blank=True)
    chapterName=models.TextField(_('chapterName'),null=True,blank=True)
    VerseID=models.BigIntegerField(null=True,blank=True)

    text = models.TextField(_('name'),null=True,blank=True)
    BookName = models.TextField(null=True,blank=True)
    Volume = models.TextField(null=True,blank=True)
    keywords=ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        )
    manyKeywords = models.ManyToManyField(Keyword)

    ##ImageFields
    # squareImage = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_square.jpg', upload_to='square')
    # landImage = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], default='default_land.jpg', upload_to='landscape')

    ##Related Fiels
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapters, null=True, blank=True, on_delete=models.CASCADE)

    # #Utility Variable

    # date_created = models.DateTimeField(blank=True, null=True)
    # last_updated = models.DateTimeField(blank=True, null=True)
    # url = models.URLField(blank=True, null=True,max_length=1000)
    class Meta:
            ordering = ['id']
    def __str__(self):
                return self.title

    def get_absolute_url(self):
                return reverse('article-detail', kwargs={'pk': self.pk})
# |       |  keywords| BookName||Volume|


class Comment(models.Model):
        post = models.ForeignKey(Articles, related_name='comments', on_delete=models.CASCADE)
        name = models.CharField(max_length=80)
        email = models.EmailField()
        body = models.TextField()

        created = models.DateTimeField(auto_now_add=True)
        active = models.BooleanField(default=False)
        updated = models.DateTimeField(auto_now=True)


        class Meta:
            ordering = ['updated']

        def __str__(self):
            return 'Comment {} by {}'.format(self.body, self.name)