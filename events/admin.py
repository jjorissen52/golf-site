from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Calendar, Book

author_extra_fieldsets = ((None, {"fields": ("dob",)}),)

class BookInline(admin.TabularInline):
    model = Book

class CalendarAdmin(PageAdmin):
    inlines = (BookInline,)
    fieldsets = deepcopy(PageAdmin.fieldsets) + author_extra_fieldsets

admin.site.register(Calendar, CalendarAdmin)