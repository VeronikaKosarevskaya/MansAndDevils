# Generated by Django 4.0.1 on 2022-01-23 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_players_options_alter_players_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='moves',
            field=models.CharField(max_length=255, verbose_name='Отчёт'),
        ),
        migrations.AlterField(
            model_name='players',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Вертухай'),
        ),
    ]
