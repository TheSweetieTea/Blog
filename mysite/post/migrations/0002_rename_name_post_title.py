# Generated by Django 4.2.1 on 2023-12-15 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='title',
        ),
    ]
