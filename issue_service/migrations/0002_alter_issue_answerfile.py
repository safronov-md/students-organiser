# Generated by Django 4.0.2 on 2022-02-18 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='answerFile',
            field=models.FileField(blank=True, default='', upload_to='static'),
        ),
    ]
