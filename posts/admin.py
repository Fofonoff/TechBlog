from django.contrib import admin

# Register your models here.
from .models import Post

# Register our Post model for the admin page to use
admin.site.register(Post)
