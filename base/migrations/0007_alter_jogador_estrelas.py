# Generated by Django 3.2.3 on 2022-12-05 13:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_pelada_quantidade_jogadores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='estrelas',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
