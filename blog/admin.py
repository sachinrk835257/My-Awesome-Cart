from django.contrib import admin
from .models import blogPost

# Register your models here.
class blogPostAdmin(admin.ModelAdmin):
    list_display = ("h1", "h2", "publish_date")

admin.site.register(blogPost,blogPostAdmin)
