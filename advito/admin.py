from django.contrib import admin
from .models import Profile, Post, Category

# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Category)