# Generated by Django 4.1 on 2022-09-06 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drinks',
            new_name='Drink',
        ),
        migrations.RenameModel(
            old_name='Subs',
            new_name='Sub',
        ),
    ]