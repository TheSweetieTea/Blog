# Generated by Django 5.0 on 2023-12-21 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_author_post_slug_comment_delete_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post'),
        ),
    ]