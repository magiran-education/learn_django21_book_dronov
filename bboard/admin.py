from django.contrib import admin

from .models import Bb, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')  # какие колонки выводить в таблице админ панели
    list_display_links = ('title', 'content')  # на какие назначить ссылки для перехода на редактирование элемента
    search_fields = ('title', 'content')  # по каким полям искать (появится строка для поиска)


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
