# Generated by Django 2.2 on 2020-08-04 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Новая')),
                ('in_progress', models.CharField(max_length=15, verbose_name='В процессе')),
                ('done', models.CharField(max_length=15, verbose_name='Выполненно')),
            ],
        ),
        migrations.CreateModel(
            name='Task_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=15, verbose_name='Задача')),
                ('bug', models.CharField(max_length=15, verbose_name='Ошибка')),
                ('enhancement', models.CharField(max_length=15, verbose_name='Улучшение')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(max_length=300, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status', to='webapp.Status', verbose_name='Статус')),
                ('type_task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type', to='webapp.Task', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
