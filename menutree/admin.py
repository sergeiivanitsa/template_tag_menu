from django.contrib import admin

from menutree.models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    """Класс для вывода модели Menu в админку"""
    list_display = ('title',)


class MenuItemAdmin(admin.ModelAdmin):
    """Класс для вывода модели MenuItem в админку"""
    list_display = ('title', 'menu', 'url', 'parent',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
