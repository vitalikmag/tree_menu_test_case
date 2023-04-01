import re

from django import template
from django.http import HttpRequest
from django.urls import reverse

from ..models import Menu

register = template.Library()


def get_menu(context, name, parent):
    current_path = ''
    url_ok = re.compile(r'^http[s]?://')
    if 'request' in context and isinstance(context['request'], HttpRequest):
        current_path = context['request'].path

    data = Menu.objects.select_related().filter(category__name=name).order_by('pk')
    menu_list = []
    for item in data:
        path = item.path.strip()
        target = '_self'
        if url_ok.match(path):
            url = path
            target = '_blank'
        else:
            url = reverse(path)

        menu_list.append({
            'id': item.pk,
            'url': url,
            'target': target,
            'name': item.name,
            'parent': item.parent_id or 0,
            'active': True if url == current_path else False,
        })

    return menu_list


@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, name='', parent=0):
    if parent != 0 and 'menu' in context:
        menu = context['menu']
    else:
        menu = get_menu(context, name, parent)

    return {
        'menu': menu,
        'current_menu': (item for item in menu if 'parent' in item and item['parent'] == parent),
    }
