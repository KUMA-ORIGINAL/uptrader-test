from django import template
from django.db.models import Prefetch

from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']

    try:
        menu = Menu.objects.prefetch_related('items__parent').get(name=menu_name)
    except Menu.DoesNotExist:
        return {
            'menu_tree': [],
            'active_item': None,
        }

    menu_items = menu.items.all()

    active_item = None
    for item in menu_items:
        if item.get_absolute_url() == request.path:
            active_item = item
            break

    def build_tree(parent=None):
        tree = []
        for item in menu_items:
            if item.parent_id == parent:
                tree.append({
                    'item': item,
                    'children': build_tree(item.id)
                })
        return tree

    menu_tree = build_tree()
    return {
        'menu_tree': menu_tree,
        'active_item': active_item,
    }
