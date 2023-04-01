from django.db import models


class Category(models.Model):
    """ Создаем категории"""
    name = models.CharField('Имя', max_length=100, blank=True)
    names = models.CharField('Имя множества', max_length=101, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Menu(models.Model):
    """Создаем модель меню"""
    name = models.CharField('Имя', max_length=128, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name='Родитель', blank=True, null=True, default=0,
                               on_delete=models.SET_DEFAULT)
    path = models.CharField('Путь', max_length=128, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись в меню'
        verbose_name_plural = 'Записи в меню'
