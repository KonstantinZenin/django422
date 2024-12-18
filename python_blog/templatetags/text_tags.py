"""
Чтобы начать использовать этот тег, нужно загрузить его в шаблон
по имени файла, в данном случае {% load text_tag %}

Потом мы можем использовать тег по имени функции {% uppercase text %}
"""
from django import template

register = template.Library()


@register.simple_tag
def uppercase(text):
    return text.upper()


@register.simple_tag
def lowercase(text):
    return text.lower()


@register.inclusion_tag('components/category_card.html')
def category_card(category):
    return {
        'name': category['name'],
        'slug': category['slug']
    }


@register.filter
def replace_spaces(text):
    return text.replace(' ', '_')
