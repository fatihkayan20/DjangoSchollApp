from django.contrib import admin
from .models import *
# Register your models here.
class odevAdmin(admin.ModelAdmin):
    fields = ['title', 'date','file']


admin.site.register(Odevler, odevAdmin)