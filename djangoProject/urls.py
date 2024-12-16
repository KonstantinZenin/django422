"""
Конверторы путей Django:
str - строки, любые символы кроме слэша '/' (по умолчанию)
int - положительные целые числа включая 0
slug - ASCII буквы/цифры, дефисы и подчеркивания
uuid - уникальные идентификаторы UUID
path - строки, включая слэши '/'

Пример использования:
path('articles/<int:year>/', views.year_archive)
path('blog/<slug:post_slug>/', views.post_detail)

"""
# Файл djangoProject
from django.contrib import admin
from django.urls import path
from python_blog.views import main
from django.urls import include

# Общий префикс posts/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    # Подключаем python_blog.urls
    path('posts/', include('python_blog.urls'))
]
