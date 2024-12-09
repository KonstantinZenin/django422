"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('djangoProject/', include('djangoProject.urls'))
"""
import python_blog.urls

# Файл из python_blog.urls
from django.contrib import admin
from django.urls import path
from python_blog.views import catalog_posts, post_detail, catalog_categories, category_datail, catalog_tags, tag_detail


urlpatterns = [
    # категории
    path('categories/', catalog_categories),
    path('categories/<slug:categories_slug>', category_datail),

    # Теги
    path('tags/', catalog_tags),
    path('tags/<slug:tags_slug>', tag_detail),

    # посты posts/tags
    path('', catalog_posts),
    path('<slug:post_slug>', post_detail),  # /posts/osnovy-python/
]
