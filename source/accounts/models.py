from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    url = models.URLField(null=True, blank=True, verbose_name='Сылка')
    about_me = models.TextField(max_length= 3000, null=True, blank=True, verbose_name='О себе')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'