# Generated by Django 2.2 on 2020-09-08 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0022_task_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='webapp.Project', verbose_name='Проект')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]
