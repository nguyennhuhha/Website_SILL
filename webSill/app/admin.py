from django.contrib import admin
from .models import *
# Register your models here.

class CollectionAdmin(admin.ModelAdmin):
   list_display = ('ID','IDtype','Name','Detail','Image','Image1','Image2','Linkdownload') 
   search_fields = ['Name']
   list_filter = ['IDtype']
admin.site.register(Collection,CollectionAdmin)

class DownloadAdmin(admin.ModelAdmin):
   list_display = ('customer','collection') 
   search_fields = ['collection']
admin.site.register(Download,DownloadAdmin)