from django.contrib import admin
from .models import Permission


# Register your models here.
class permissionAdmin(admin.ModelAdmin):
    fields = ['title', 'content','event_start_date','event_end_date']

admin.site.register(Permission, permissionAdmin)
