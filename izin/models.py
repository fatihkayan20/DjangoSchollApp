from django.db import models


# Create your models here.
from django.utils.text import slugify


class Permission(models.Model):
    title = models.CharField(max_length=50,unique=True, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Zamanı')
    event_start_date = models.DateTimeField(auto_now_add=False, verbose_name='Etkinlik Başlangıcı')
    event_end_date = models.DateTimeField( auto_now_add=False,verbose_name='Etkinlik Bitisi')
    accept = models.ManyToManyField('auth.User',related_name='accept', verbose_name='Kabul')
    veto = models.ManyToManyField('auth.User',related_name='veto', verbose_name='Red')
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Permission,self).save(*args, **kwargs)