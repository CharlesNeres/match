# Generated by Django 3.2.3 on 2022-12-03 16:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_pelada_quantidade_jogadores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='estrelas',
            field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
