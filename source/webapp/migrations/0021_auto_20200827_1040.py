# Generated by Django 2.2 on 2020-08-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_auto_20200827_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(verbose_name='Дата начала'),
        ),
    ]
