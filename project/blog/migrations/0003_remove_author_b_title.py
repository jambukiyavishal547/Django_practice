# Generated by Django 5.0.4 on 2024-05-08 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_b_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='b_title',
        ),
    ]
