# Generated by Django 3.0.3 on 2020-06-03 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_updated',
        ),
    ]
