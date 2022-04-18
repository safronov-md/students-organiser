# Generated by Django 4.0.2 on 2022-04-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_data', models.JSONField()),
                ('type', models.CharField(max_length=10)),
                ('assignee', models.IntegerField()),
                ('category', models.IntegerField()),
                ('attachments', models.FileField(upload_to='')),
            ],
        ),
    ]