# Generated by Django 3.2.3 on 2022-12-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20221203_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelada',
            name='quantidade_jogadores',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]