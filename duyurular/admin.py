from django.contrib import admin
from .models import *


# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    fields = ['title', 'content']


admin.site.register(Notification,NotificationAdmin )
