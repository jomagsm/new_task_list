# Generated by Django 2.2 on 2020-08-15 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20200812_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание'),
        ),
    ]
