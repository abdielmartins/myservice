# Generated by Django 2.2.13 on 2020-06-16 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0009_auto_20200615_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validation',
            name='birth_date',
            field=models.CharField(max_length=10),
        ),
    ]