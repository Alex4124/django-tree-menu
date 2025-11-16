from django import template
from django.urls import reverse, NoReverseMatch
from tree_menu.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_slug):
    
    request = context['request']
    current_url = request.path
    
    try:
        menu = Menu.objects.get(slug=menu_slug)
    except Menu.DoesNotExist:
        return {'menu_items': []}

    menu_items = MenuItem.objects.filter(menu=menu).select_related('parent')
 
    active_item = None
    items_to_expand = set()
    
    for item in menu_items:
        item_url = get_item_url(item)
        if item_url == current_url:
            active_item = item
            break
    
    if active_item:
        
        current = active_item
        while current:
            items_to_expand.add(current.id)
            current = current.parent
        

        for item in menu_items:
            if item.parent_id == active_item.id:
                items_to_expand.add(item.id)
    
    root_items = [item for item in menu_items if item.parent_id is None]
    
    return {
        'menu_items': root_items,
        'all_items': list(menu_items),
        'active_item': active_item,
        'items_to_expand': items_to_expand,
        'current_url': current_url,
    }


def get_item_url(item):
    if item.url:
        return item.url
    elif item.named_url:
        try:
            return reverse(item.named_url)
        except NoReverseMatch:
            return '#'
    return '#'


@register.simple_tag
def get_url(item):
    return get_item_url(item)

@register.filter
def children_of(items, parent):
    return [item for item in items if item.parent_id == parent.id]
