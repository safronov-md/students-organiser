# Generated by Django 4.0.2 on 2022-02-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_service', '0011_alter_schedule_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='order',
        ),
        migrations.AddField(
            model_name='schedule',
            name='time',
            field=models.CharField(choices=[('08:00 - 09:30', '08:00 - 09:30'), ('09:45 - 11:15', '09:45 - 11:15'), ('11:30 - 13:00', '11:30 - 13:00'), ('13:30 - 15:00', '13:30 - 15:00'), ('15:15 - 16:45', '15:15 - 16:45'), ('17:00 - 18:30', '17:00 - 18:30')], default='UnTimed', max_length=25),
        ),
    ]
