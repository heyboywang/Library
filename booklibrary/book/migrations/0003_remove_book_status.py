# Generated by Django 2.2 on 2019-04-28 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='status',
        ),
    ]