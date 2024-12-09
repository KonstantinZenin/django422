from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse('Главная страница')


def catalog_posts(request):
    return HttpResponse('Каталог постов')


def post_detail(request, post_slug):
    return HttpResponse(f'Страница поста {post_slug}')


def catalog_categories(request):
    return HttpResponse(f'Каталог категорий')


def category_datail(request, categories_slug):
    return HttpResponse(f'Страница категории {categories_slug}')


def catalog_tags(request):
    return HttpResponse(f'Каталог тегов')


def tag_detail(request, tags_slug):
    return HttpResponse(f'Страница тега {tags_slug}')
