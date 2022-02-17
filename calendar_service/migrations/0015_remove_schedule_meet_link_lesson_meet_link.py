# Generated by Django 4.0.2 on 2022-02-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_service', '0014_schedule_meet_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='meet_link',
        ),
        migrations.AddField(
            model_name='lesson',
            name='meet_link',
            field=models.CharField(default='https://google.com/', max_length=255),
        ),
    ]
