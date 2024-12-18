from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# python manage.py runserver запуск сервера

CATEGORIES = [
    {'slug': 'python', 'name': 'Python'},
    {'slug': 'django', 'name': 'Django'},
    {'slug': 'postgresql', 'name': 'PostgreSQL'},
    {'slug': 'docker', 'name': 'Docker'},
    {'slug': 'linux', 'name': 'Linux'},
]

def main(request):
    catalog_categories_url = reverse('blog:categories')
    catalog_tags_url = reverse('blog:tags')
    context = {"title": "Главная",
               "text": "Текст главной страницы",
               "user_status": "admin",
               # "menu_items": MENU_ITEMS,
               }
    return render(request, "main.html", context=context)


def catalog_posts(request):
    return HttpResponse('Каталог постов')


def post_detail(request, post_slug):
    return HttpResponse(f'Страница поста {post_slug}')


def catalog_categories(request):
    links = []
    for category in CATEGORIES:
        url = reverse('blog:category_datail', args=[category['slug']])
        links.append(f'<p><a href="{url}">{category["name"]}</a></p>')

    context = {
        'title': "Категории",
        'text': "Текст страницы с категориями",
        "categories": CATEGORIES,
    }

    return render(request, "catalog_categories.html", context=context)


def category_datail(request, categories_slug):
    category = next((cat for cat in CATEGORIES
    if cat['slug'] == categories_slug), None)
    if category:
        name = category['name']
    else:
        name = categories_slug

    context = {
        "title": f"Категория {name}",
        "text": f"Текст категории {name}",
    }

    return render(request, "category_detail.html", context)


def catalog_tags(request):
    return HttpResponse(f'Каталог тегов')


def tag_detail(request, tags_slug):
    return HttpResponse(f'Страница тега {tags_slug}')
