# Generated by Django 4.0.2 on 2022-02-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_service', '0008_alter_schedule_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='title',
            field=models.CharField(choices=[('[LAB] ASDC', '[LAB] ASDC'), ('[LAB] Web programming', '[LAB] Web programming'), ('[LAB] CNMO', '[LAB] CNMO'), ('[LAB] AI', '[LAB] AI'), ('[CURS] Sport Eduaction', '[CURS] Sport Eduaction'), ('[LAB] Java Programming', '[LAB] Java Programming'), ('[CURS] Cryptography', '[CURS] Cryptography'), ('[CURS] AI', '[CURS] AI'), ('[CURS] Algorithms', '[CURS] Algorithms'), ('[LAB] Cryptography', '[LAB] Cryptography'), ('[CURS] Web programming', '[CURS] Web programming'), ('[CURS] Java Programming', '[CURS] Java Programming'), ('[CURS] CNMO', '[CURS] CNMO'), ('[LAB] Test', '[LAB] Test')], max_length=250),
        ),
    ]