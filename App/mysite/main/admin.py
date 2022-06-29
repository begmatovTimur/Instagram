from django.contrib import admin
from main.models import Post, User, Category, Comment


admin.site.register(Post)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Comment)