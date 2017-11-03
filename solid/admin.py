from copy import deepcopy
from django.contrib import admin
from mezzanine.galleries.admin import GalleryAdmin
from mezzanine.galleries.models import Gallery

blog_fieldsets = deepcopy(GalleryAdmin.fieldsets)

class MyGalleryAdmin(GalleryAdmin):
    fieldsets = blog_fieldsets

admin.site.unregister(Gallery)
admin.site.register(Gallery, MyGalleryAdmin)
