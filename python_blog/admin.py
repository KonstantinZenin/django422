from django.contrib import admin
from python_blog.models import Category, Post

# Регистрация 2 способами
"""
1. Регистрация с использованием функции register
2. Регистрация м использованием класса
"""

# 1. Регистрация с использованием функции
admin.site.register(Category)


# 2. Регистрация м использованием класса
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ["title", "created_at", "updated_at", "category"]


admin.site.register(Post, PostAdmin)
