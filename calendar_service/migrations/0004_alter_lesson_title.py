# Generated by Django 4.0.2 on 2022-02-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_service', '0003_lesson_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
