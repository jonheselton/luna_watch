# Generated by Django 5.0.6 on 2024-08-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_luna_watch', '0002_rename_pet_name_schedule_pet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='visits_per_day',
            field=models.IntegerField(default=3),
        ),
    ]