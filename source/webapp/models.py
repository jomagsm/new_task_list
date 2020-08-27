from django.db import models
from django.core.validators import MinLengthValidator

STATUS_CHOICE = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
TYPE_CHOICE = [('Task', 'Задача'), ('Bug', 'Ошибка'), ('Enhancement', 'Улучшение')]


class Status(models.Model):
    name = models.CharField(max_length=15, verbose_name='Статус')

    def __str__(self): return self.name

STATUS_CHOICE2 = [Status.objects.all()]


class Task_type(models.Model):
    name = models.CharField(max_length=15, verbose_name='Тип')

    def __str__(self): return self.name

TYPE_CHOICE2 = [Task_type.objects.all()]


class Task(models.Model):
    project_pk = models.ForeignKey('webapp.Project', related_name='project', verbose_name='Проект', on_delete=models.CASCADE)
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length= 3000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.PROTECT, verbose_name='Статус')
    type_task = models.ManyToManyField('webapp.Task_type', related_name='type', verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_deleted = models.BooleanField(default=False,verbose_name='Мягкое удаление')

    def __str__(self):
        return "{}. {}".format(self.project_pk, self.pk, self.summary)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Project(models.Model):
    start_date = models.DateField(verbose_name='Дата начала')
    finish_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

