from django.db import models


class Players(models.Model):
    name = models.CharField(max_length=255, verbose_name='Вертухай')
    sex = models.CharField(max_length=255, verbose_name='Кто по жизни')
    years_old = models.IntegerField(verbose_name='На сколько преисполнен')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата смены')
    real_home = models.CharField(max_length=255, verbose_name='Исходное')
    moves = models.CharField(max_length=255, verbose_name='Отчёт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Наши спонсоры'
        verbose_name_plural = 'Наши спонсоры'
        ordering = ('time_create',)


# class Explode(models.Model):
#     moves = models.CharField(max_length=255, verbose_name='Отчёт')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Explode'
#         verbose_name_plural = 'Explode'
#         ordering = ('id',)
