# Generated by Django 2.2.13 on 2020-06-15 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0004_auto_20200615_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='validation',
            old_name='user',
            new_name='uservalid',
        ),
    ]
