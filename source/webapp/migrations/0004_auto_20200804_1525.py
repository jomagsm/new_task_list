# Generated by Django 2.2 on 2020-08-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200804_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='done',
        ),
        migrations.RemoveField(
            model_name='status',
            name='in_progress',
        ),
        migrations.RemoveField(
            model_name='status',
            name='new',
        ),
        migrations.RemoveField(
            model_name='task_type',
            name='bug',
        ),
        migrations.RemoveField(
            model_name='task_type',
            name='enhancement',
        ),
        migrations.RemoveField(
            model_name='task_type',
            name='task',
        ),
        migrations.AddField(
            model_name='status',
            name='name',
            field=models.CharField(default='New', max_length=15, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='task_type',
            name='name',
            field=models.CharField(default='Bug', max_length=15, verbose_name='Тип'),
        ),
    ]
