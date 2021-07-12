from django.contrib import admin
from .models import Project, ProjectImage

# Register your models here.


class  ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)

