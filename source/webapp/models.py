from django.db import models
from django.utils import timezone


STATUS_CHOICE = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Status(models.Model):
    name = models.CharField(max_length=15, verbose_name='Новая')
    in_progress = models.CharField(max_length=15, verbose_name='В процессе')
    done = models.CharField(max_length=15, verbose_name='Выполненно')



class Article(models.Model):
    name = models.TextField(max_length=1000, null=False, default=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=40, choices=STATUS_CHOICE, default='new')
    create_at = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Task_type(models.Model):
    task = models.CharField(max_length=15, verbose_name='Задача')
    bug = models.CharField(max_length=15, verbose_name='Ошибка')
    enhancement = models.CharField(max_length=15, verbose_name='Улучшение')


class Task(models.Model):
   article = models.ForeignKey('webapp.Article', related_name='comments', on_delete=models.CASCADE, verbose_name='Статья')
   summary = models.TextField(max_length= 300, verbose_name='Заголовок')
   description = models.TextField(max_length= 3000, null=True, blank=True, verbose_name='Описание')
   status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.PROTECT, verbose_name='Статус')
   type_task = models.ForeignKey('webapp.Task', related_name='type', on_delete=models.PROTECT, verbose_name='Тип')
   created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


   def __str__(self):
       return self.text[:20]

