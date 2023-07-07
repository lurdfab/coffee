from django.contrib import admin
from .models import *

# Register your models here.

class AppInfoAdmin(admin.ModelAdmin):
     list_display = ('id', 'appname')

class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('id','name', 'old_price', 'new_price', 'upload_at', 'updated_at')

class ProductsAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug':('name',)}
     list_display = ('id','name', 'old_price', 'new_price', 'upload_at', 'updated_at')

class ContactAdmin(admin.ModelAdmin):
     list_display = ('name', 'email', 'phone', 'message', 'sent')

class RegisterAdmin(admin.ModelAdmin):
     list_display = ('first_name', 'last_name', 'email', 'phone', 'address')

class ReviewsAdmin(admin.ModelAdmin):
     list_display = ('id', 'user', 'comment', 'rating', 'created_at', 'updated_at')

admin.site.register(AppInfo, AppInfoAdmin)
admin.site.register(AboutUs)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Register, RegisterAdmin)
admin.site.register(Reviews, ReviewsAdmin)
