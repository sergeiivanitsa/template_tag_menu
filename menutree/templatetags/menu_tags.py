from django import template

from menutree.models import MenuItem

register = template.Library()


@register.inclusion_tag('menutree/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """Функция для регистрации собственного тега
    для вывода меню на страницу"""
    active_menu = context['request'].path
    structure_menu = {}
    parent_id = None
    active_menu_id = None
    item_menu = MenuItem.objects.filter(
            menu__title=menu_name
        ).select_related('parent', 'menu').order_by('parent')
    for item in item_menu:
        if item.get_absolute_url() == active_menu:
            parent_id = item.get_parent_id()
            active_menu_id = item.id
        if not item.parent:
            structure_menu[item] = []
        else:
            for k, v in structure_menu.items():
                if item.parent == k:
                    structure_menu[k].append(item)
                    break
                if item.parent in v:
                    index = structure_menu[k].index(item.parent)
                    structure_menu[k][index] = {item.parent: [item]}
                    break
                for sub_menu in v:
                    if isinstance(
                        sub_menu, dict
                    ) and item.parent == list(sub_menu.keys())[0]:
                        sub_menu[item.parent].append(item)
                        break
    print(structure_menu)
    return {'menu_dict': structure_menu,
            'parent_id': parent_id,
            'active_menu_id': active_menu_id}


@register.filter
def get_key_from_dict(value):
    if isinstance(value, dict):
        return list(value.keys())[0]
    else:
        return value


@register.filter
def get_values_from_dict(value):
    if isinstance(value, dict):
        return list(value.values())[0]
    else:
        return value
