from django.contrib import admin

from rango.models import Category, Page

from rango.models import UserProfile

class PageAdmin (admin.ModelAdmin):
    list_display = ( 'title', 'category', 'url',)

admin.site.register(Page, PageAdmin)

class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')
    # Add in this class to customize the Admin Interface
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)