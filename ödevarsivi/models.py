from django.db import models
from django import forms

# Create your models here.
from django.utils.text import slugify


class Odevler(models.Model):
    class Meta:
        verbose_name_plural = 'Ödevler'
    title=models.CharField(max_length=50,verbose_name='Ödev Adı', unique=True)
    date=models.DateTimeField(auto_now_add=False,verbose_name='Tarih')
    file=models.FileField(upload_to="pdf/odev-arsiv",verbose_name='Dosya')
    slug = models.SlugField(max_length=100)
    published_date=models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Odevler,self).save(*args, **kwargs)

