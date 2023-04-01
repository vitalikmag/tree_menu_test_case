from django.contrib import admin

from .models import Category, Menu


@admin.register(Menu)
class TreeMenuAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'parent', 'path', ]
    list_display = ['__str__', 'category', 'parent', 'path', ]


@admin.register(Category)
class TreeMenuCategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'names', ]
    list_display = ['__str__', ]
