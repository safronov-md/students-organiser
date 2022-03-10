# Generated by Django 4.0.2 on 2022-02-23 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store_service', '0004_alter_storage_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
