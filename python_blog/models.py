from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(null=True, blank=True, max_length=100)

# PRICTICE - Работа с моделью Post
"""
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

"""