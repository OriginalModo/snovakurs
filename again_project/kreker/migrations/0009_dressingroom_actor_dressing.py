# Generated by Django 4.1.6 on 2023-02-04 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kreker', '0008_actor_movie_actors'),
    ]

    operations = [
        migrations.CreateModel(
            name='DressingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='dressing',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kreker.dressingroom'),
        ),
    ]
