# Generated by Django 4.0.2 on 2022-04-18 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_events_assignee_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='attachments',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]