from django.contrib import admin

# a new import
from blogging.models import Post, Category

# and a new admin registration
admin.site.register(Post)
admin.site.register(Category)
