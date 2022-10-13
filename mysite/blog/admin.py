from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Category, Post, Comment


# Register your models here.

# for configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("image_tag", "title", "description", "url", "add_date")
    search_fields = ("title",)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    list_filter = ("cat",)
    list_per_page = 50


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

admin.site.register(Comment)
