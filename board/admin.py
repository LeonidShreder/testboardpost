from django.contrib import admin
from .models import Comments, Post


class PostInline(admin.StackedInline):
    model = Comments
    extra = 1


class PostAdmin(admin.ModelAdmin):
    fields = ['author_name', 'text']
    inlines = [PostInline]
    list_filter = ['date']


admin.site.register(Post, PostAdmin)
