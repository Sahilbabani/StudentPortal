# Generated by Django 2.1.4 on 2018-12-25 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internship',
            name='experience_needed',
        ),
        migrations.RemoveField(
            model_name='internship',
            name='joining_date',
        ),
        migrations.RemoveField(
            model_name='placement',
            name='experience_needed',
        ),
        migrations.AddField(
            model_name='internship',
            name='test_location',
            field=models.TextField(default=''),
        ),
    ]
