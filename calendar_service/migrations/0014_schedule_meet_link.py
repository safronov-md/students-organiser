# Generated by Django 4.0.2 on 2022-02-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_service', '0013_schedule_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='meet_link',
            field=models.CharField(default='https://google.com/', max_length=255),
        ),
    ]