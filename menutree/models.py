from django.db import models


class Menu(models.Model):
    """Модель для меню"""
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    """Модель для пунктов меню"""
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='menu_items'
    )
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.parent:
            return '/category/%s/%s/%s' % (self.menu, self.parent, self.title)
        else:
            return '/category/%s/%s' % (self.menu, self.title)

    def get_parent_id(self):
        if self.parent:
            return self.parent.id

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
