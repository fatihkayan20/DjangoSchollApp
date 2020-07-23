from django.contrib import admin
from .models import *


# Register your models here.
class fotoAdmin(admin.StackedInline):
    model = FotoImage



@admin.register(Fotograflar)
class FotograffAdmin(admin.ModelAdmin):
    inlines = [fotoAdmin]
    fields = ('title','date',)

    class Meta:
        model = Fotograflar


@admin.register(FotoImage)
class arsivImageAdmin(admin.ModelAdmin):
    pass
