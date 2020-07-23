from django.db import models

# Create your models here.
from django.utils.text import slugify


class Fotograflar(models.Model):
    class Meta:
        verbose_name_plural = 'Fotoğraflar'
    title=models.CharField(max_length=50,verbose_name='Başlık', unique=True)
    date=models.DateTimeField(auto_now_add=False,verbose_name='Tarih')
    image=models.ImageField(verbose_name='Fotoğraflar', blank=True, null=False)
    slug = models.SlugField(max_length=100)
    published_date=models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Fotograflar,self).save(*args, **kwargs)

class FotoImage(models.Model):
    arsiv=models.ForeignKey(Fotograflar,default=None,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.arsiv.title
