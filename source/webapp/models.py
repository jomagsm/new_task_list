from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=15, verbose_name='Новая')
    in_progress = models.CharField(max_length=15, verbose_name='В процессе')
    done = models.CharField(max_length=15, verbose_name='Выполненно')


class Task_type(models.Model):
    task = models.CharField(max_length=15, verbose_name='Задача')
    bug = models.CharField(max_length=15, verbose_name='Ошибка')
    enhancement = models.CharField(max_length=15, verbose_name='Улучшение')


class Task(models.Model):
    summary = models.TextField(max_length= 300, verbose_name='Заголовок')
    description = models.TextField(max_length= 3000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.PROTECT, verbose_name='Статус')
    type_task = models.ForeignKey('webapp.Task', related_name='type', on_delete=models.PROTECT, verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return "{}. {}".format(self.pk, self.summary)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'