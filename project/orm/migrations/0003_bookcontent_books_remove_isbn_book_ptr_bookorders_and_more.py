# Generated by Django 5.0.4 on 2024-05-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0002_book_isbn'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='isbn',
            name='book_ptr',
        ),
        migrations.CreateModel(
            name='BookOrders',
            fields=[
            ],
            options={
                'ordering': ['created'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('orm.bookcontent',),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='ISBN',
        ),
    ]
