from django.contrib import admin
from blog.models import Tag, Post


class PostAdmin(admin.ModelAdmin):
  populated_fields = {"slug": ("title",)}
  list_dislplay = ('slug','published_at')

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
