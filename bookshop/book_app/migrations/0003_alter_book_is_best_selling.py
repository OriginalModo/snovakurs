# Generated by Django 4.1.5 on 2023-02-04 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_book_is_best_selling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='is_best_selling',
            field=models.BooleanField(default=True, null=True),
        ),
    ]