from django.contrib import admin
from .models import Brand,Category,Products,Comment
from django.db import models




# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':('brand_name',)
    }
admin.site.register(Brand,BrandAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':('category_name',)
    }
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['pr_name','brand','category','price','available']

    list_display_links = ['pr_name','brand']
    list_editable = ['price','available']
    search_fields = ['pr_name']
    list_filter = ['brand','category','price','available']

admin.site.register(Products,ProductAdmin)
admin.site.register(Comment)