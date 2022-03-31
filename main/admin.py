from django.contrib import admin

from main.models import Category, Apartment, Image


class ImageInLineAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 10

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    inlines = [ImageInLineAdmin,]

admin.site.register(Category)

