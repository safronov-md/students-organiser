# Generated by Django 4.0.2 on 2022-04-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='assignee_type',
            field=models.CharField(default='group', max_length=15),
            preserve_default=False,
        ),
    ]
