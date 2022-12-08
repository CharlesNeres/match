# Generated by Django 3.2.3 on 2022-12-03 13:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelada',
            fields=[
                ('id_pelada', models.AutoField(primary_key=True, serialize=False)),
                ('nome_pelada', models.CharField(max_length=50)),
                ('quantidade_jogadores', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pelada',
            },
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id_jogador', models.AutoField(primary_key=True, serialize=False)),
                ('nome_jogador', models.CharField(max_length=50)),
                ('estrelas', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('tipo_jogador', models.CharField(choices=[('GOLEIRO', 'Goleiro'), ('ZAGUEIRO', 'Zagueiro'), ('MEIO CAMPO', 'Meio Campo'), ('ATACANTE', 'Atacante')], max_length=15)),
                ('jogador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.pelada')),
            ],
            options={
                'db_table': 'jogador',
            },
        ),
    ]
