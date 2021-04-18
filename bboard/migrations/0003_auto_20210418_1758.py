# Generated by Django 2.1.3 on 2021-04-18 14:58

import bboard.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20210414_2156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bb',
            options={'get_latest_by': ['published'], 'ordering': ['-published'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AddField(
            model_name='bb',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активно'),
        ),
        migrations.AddField(
            model_name='bb',
            name='kind',
            field=models.CharField(choices=[('b', 'Куплю'), ('s', 'Продам'), ('c', 'Обменяю')], default='b', max_length=1, verbose_name='Действие'),
        ),
        migrations.AddField(
            model_name='rubric',
            name='show',
            field=models.BooleanField(default=True, null=True, verbose_name='Отображать'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='content',
            field=models.TextField(blank=True, null=True, validators=[bboard.validators.NotNumberValidator], verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(limit_choices_to={'show': True}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entries', related_query_name='entry', to='bboard.Rubric', verbose_name='Рубрика'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(error_messages={'invalid': 'Неправильное название товара'}, max_length=50, validators=[bboard.validators.not_number_validator], verbose_name='Товар'),
        ),
        migrations.AddIndex(
            model_name='bb',
            index=models.Index(fields=['-published', 'title'], name='main'),
        ),
        migrations.AddIndex(
            model_name='bb',
            index=models.Index(fields=['title', 'price', 'rubric'], name='bboard_bb_title_e42980_idx'),
        ),
    ]