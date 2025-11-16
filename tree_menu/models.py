from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name="Название меню")
    slug = models.SlugField(max_length=256, unique=True, verbose_name="Slug")

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название пункта")
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE, verbose_name="Меню")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE, verbose_name="Родительский пункт")
    url = models.CharField(max_length=256, blank=True, verbose_name="URL")
    named_url = models.CharField(max_length=256, blank=True, verbose_name="Named URL")
    order = models.IntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
        ordering = ['order', 'id']

    def __str__(self):
        return self.name
