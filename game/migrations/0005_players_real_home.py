# Generated by Django 4.0.1 on 2022-01-31 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_players_moves_alter_players_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='real_home',
            field=models.CharField(default=1235, max_length=255, verbose_name='Исходное'),
            preserve_default=False,
        ),
    ]
