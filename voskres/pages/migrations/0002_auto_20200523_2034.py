# Generated by Django 3.0.6 on 2020-05-24 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='order',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='visible_in_menu',
        ),
    ]