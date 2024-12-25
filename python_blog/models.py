from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        'Category',  # Ссылка на модель Category
        on_delete=models.SET_DEFAULT,  # При удалении категории, установить значение NULL
        blank=True,  # Не требуем в формах заполнения
        null=True,  # Разрешаем значение NULL в базе данных
        related_name="posts",  # Имя обратно связи
        default=None
    )


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True, null=True, default="Без описания")


# PRICTICE - Работа с моделью Post
"""
0.Запуск Shell Plus
 python manage.py shell_plus --print-sql

1. Создать новый пост
post = Post(title="Django для чаников", content="Django очень простой фреймворк, и у него пологая кривая входа...")
post.save()

INSERT INTO "python_blog_post" ("title", "content", "created_at", "updated_at", "category")
VALUES ('Django для чаников', 'Django очень простой фреймворк, и у него пологая кривая
 входа...', '2024-12-23 17:31:24.936493', '2024-12-23 17:31:24.936493', NULL) RETURNING "python_blog_post"."id"
Execution time: 0.013149s [Database: default]

post_1 = post

post_2 = Post(title="Базы данных для продавцов котиков", content="Теперь вы сможете каждого котика сохранить в базе данных")

post_2.save()

INSERT INTO "python_blog_post" ("title", "content", "created_at", "updated_at", "category")
VALUES ('Базы данных для продавцов котиков', 'Теперь вы сможете каждого котика сохрани
ть в базе данных', '2024-12-23 17:35:42.321533', '2024-12-23 17:35:42.321533', NULL) RETURNING "python_blog_post"."id"
Execution time: 0.002429s [Database: default]

Django ORM ленива.
Все запросы по умолчанию выполняются в ленивом режиме.
Допустим при сохранении, запрос будет выполнен только при вызове метода save()

При чтении, запрос будет выполнен при обращении к результату запроса

2. Получить все посты
posts = Post.objects.all()
posts = <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>]>

Что такое QuerySet?
QuerySet - это набор объектов, которые мы получили из базы данных.
Мы можем использовать QuerySet для фильтрации, сортировки, группировки и других операций над объектами.

post_1 = posts[0]
post_1

post_1.title
post_1.content
post_1.created_at

post_1.content = "Django не очень простой фреймворк, но у него пологая кривая входа..."
post_1.title = "Django для чайников"

post_3 = Post(title="Тестовый пост", content="Тестовый пост")
post_3.save()

# Делаем операцию удаления
post_3.delete()

DELETE
  FROM "python_blog_post"
 WHERE "python_blog_post"."id" IN (3)
Execution time: 0.006675s [Database: default]

3. Получить пост по id
post_1 = Post.objects.get(id=1) # id - поле модели id -это поле, которое автоматически генерируется Django/
post_1 = Post.objects.get(id=1) # pk - primary key - первичны ключ

4. Получим все посты и сортируем их по полю created_at от новых к старым
posts = Post.objects.all().order_by("-created_at")

SELECT "python_blog_post"."id",
       "python_blog_post"."title",
       "python_blog_post"."content",
       "python_blog_post"."created_at",
       "python_blog_post"."updated_at",
       "python_blog_post"."category"
  FROM "python_blog_post"
 ORDER BY "python_blog_post"."created_at" DESC
 
5. Используя filter получим посты где категория NULL
posts = Post.objects.filter(category=None)
Применим к полученному QuerySet сортировку
posts = Post.objects.order_by("-created_at")
"""

# PRICTICE - Работа с моделью Category
"""
0.Запуск Shell Plus
python manage.py shell_plus --print-sql
 
1. Создать новую категорию
    {'slug': '', 'name': ''},
    {'slug': 'django', },
    {'slug': 'postgresql', 'name': 'PostgreSQL'},
    {'slug': 'docker', 'name': ''},
    {'slug': 'linux', 'name': 'Linux'},
category_1 = Category( name='Django', slug='django').save()
category_2 = Category( name='Python', slug='python').save()
category_3 = Category( name='PostgreSQL', slug='postgresql').save()
category_4 = Category( name='Docker', slug='docker').save()
category_5 = Category( name='Linux', slug='linux').save()

2. Получим все посты
posts = Post.objects.all()

3. Возьмём первый пост
post_1 = posts[0]

django_category = Category.objects.get(name='Django')

4. post_1 - хочу присвоить категорию
post_1.category = django_category
post_1.save()

post_1  - это объект, который мы получили из базы данных
post_1.title - это поле title у объекта post_1
post_1.category - экземпляр объекта Category, который мы присвоили объекту post_1

post_1.category.name - Django

# Обратное связывание. Мы обозначили related_name="posts" в модели Post

# Получим все посты по объекту категории
category = Category.objects.get(name='Django')
django_posts = category.posts.all()

# Если бы не было related_name="posts"
category = Category.objects.get(name='Django')
django_posts = Post.objects.filter(category=category)

# или
django_posts = Post.objects.filter(category__name='Django')
"""
