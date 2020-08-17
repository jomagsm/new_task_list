# Generated by Django 2.2 on 2020-08-12 16:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_remove_task_type_task_old'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=3000, null=True, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Описание'),
        ),
    ]