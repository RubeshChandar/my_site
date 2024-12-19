from django.contrib import admin
from .models import Author, Post, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("date", "title", "author",)
    prepopulated_fields = {"slug": ("title",)}


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
