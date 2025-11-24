from django.contrib import admin
from .models import Task, SubTask, Category

""" Из трех вариантов регистрации классов выбираю через Декоратор.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask, SubTaskAdmin)
таким образом выглядела бы регистрация без декоратора

"""


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Task, )
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'deadline', 'created_at')
    list_filter = ('status', 'categories')
    search_fields = ('title', 'status')
    filter_horizontal = ('categories',)


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'status', 'deadline', 'created_at')
    list_filter = ('status', 'task')
    search_fields = ('title', 'status')