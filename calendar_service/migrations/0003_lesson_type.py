# Generated by Django 4.0.2 on 2022-02-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_service', '0002_lesson_alter_schedule_day_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='type',
            field=models.CharField(choices=[('LAB', 'LAB'), ('CURS', 'CURS')], default='CURS', max_length=4),
        ),
    ]
