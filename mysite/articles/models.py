
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


class Category(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    # slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    # date_created = models.DateTimeField(blank=True, null=True)
    # last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.title)


    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})


#     def save(self, *args, **kwargs):
#         if self.date_created is None:
#             self.date_created = timezone.localtime(timezone.now())
#         if self.uniqueId is None:
#             self.uniqueId = str(uuid4()).split('-')[4]
#             self.slug = slugify('{} {}'.format(self.title, self.uniqueId))


#         self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
#         self.last_updated = timezone.localtime(timezone.now())
#         super(Category, self).save(*args, **kwargs)




class Articles(models.Model):
    title = models.TextField(null=True)
    desc = models.TextField(null=True)
    photo = models.ImageField(null=True,blank=True,upload_to='photos')
    file = models.FileField(null=True,blank=True,upload_to ='files/% Y/% m/% d/')

    content = models.TextField(null=True)
    hashtags = models.CharField(null=True, blank=True, max_length=300)

    ##ImageFields
    # squareImage = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_square.jpg', upload_to='square')
    # landImage = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], default='default_land.jpg', upload_to='landscape')

    ##Related Fiels
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    #Utility Variable

    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    url = models.URLField(blank=True, null=True,max_length=1000)
   
    def __str__(self):
                return self.title

    def get_absolute_url(self):
                return reverse('article-detail', kwargs={'pk': self.pk})

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