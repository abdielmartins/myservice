# Generated by Django 2.2.13 on 2020-06-15 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0002_auto_20200615_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='validation',
            name='city',
            field=models.CharField(default='Curitiba', max_length=30),
        ),
    ]