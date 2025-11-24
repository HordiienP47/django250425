from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)  # это поле от себя вне задания
    # Добавил поле описание с пустыми скобками, без default, null... при создании миграции
    # получил предупреждение Please select a fix:

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_category_name')
        ] # можно использовать и unique_together, но как Вы сказали в лекции constraints более универсальный
          # как сказала Алена на лекции на будущее для расширения возможностей

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('pending', 'Pending'),
        ('blocked', 'Blocked'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=120)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_task_title')
        ]

class SubTask(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In progress'),
        ('pending', 'Pending'),
        ('blocked', 'Blocked'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=120)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} → {self.task.title}"

    class Meta:
        db_table = 'task_manager_subtask'
        verbose_name = 'SubTask'
        verbose_name_plural = 'SubTasks'
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_subtask_title')
        ]