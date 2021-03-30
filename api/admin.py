from django.contrib import admin
from .models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin
 

## Import Export class for save data
class PorfolioResource(resources.ModelResource):
    class Meta:
        model = Porfolio

class BlogResource(resources.ModelResource):
    class Meta:
        model = Blogs


class PorfolioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name_project','source_code')
    resource_class = PorfolioResource

class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title','author','publish_date')
    resource_class = BlogResource


# Register your models here.
admin.site.register(Porfolio, PorfolioAdmin)
admin.site.register(Blogs, BlogAdmin)