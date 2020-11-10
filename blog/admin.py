from django.contrib import admin
from .models import Post

# Register your models here.

# Registering Post model to our admin page, so we have GUI to add, delete, edit
admin.site.register(Post)
