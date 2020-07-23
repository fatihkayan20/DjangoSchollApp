from django.db import models

# Create your models here.
from django.utils.text import slugify


class Notification(models.Model):
    title = models.CharField(max_length=100,verbose_name='Başlık',unique=True,)
    content = models.TextField(verbose_name='İçerik')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Zamanı')
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Notification,self).save(*args, **kwargs)