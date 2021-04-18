from django.db import models
from bboard.validators import min_5_chars


class Bb(models.Model):
    BUY = 'b'
    SALE = 's'
    CHANGE = 'c'
    KINDS = (
        (BUY, 'Куплю'),
        (SALE, 'Продам'),
        (CHANGE, 'Обменяю'),
    )

    title = models.CharField(max_length=50, verbose_name='Товар', validators=[min_5_chars],
                             error_messages={'invalid': 'Неправильное название товара'})
    content = models.TextField(null=True, blank=True, verbose_name='Описание', validators=[min_5_chars])
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT, null=True, limit_choices_to={'show': True},
                               related_name='entries', related_query_name='entry',
                               verbose_name='Рубрика')
    is_active = models.BooleanField(default=True, verbose_name='Активно')
    kind = models.CharField(max_length=1, choices=KINDS, verbose_name='Действие', default=BUY)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Объявления'  # название элементов модели во множественном числе
        verbose_name = 'Объявление'  # в единственном числе
        ordering = ['-published']  # сортировка по умолчанию
        get_latest_by = ['published']  # имя поля по которому определяются самый ранний и поздний элементы: функции
        # latest() и earliest()
        indexes = [
            models.Index(fields=['-published', 'title'], name='main'),
            models.Index(fields=['title', 'price', 'rubric'])
        ]


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    show = models.BooleanField(default=True, null=True, verbose_name='Отображать')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
