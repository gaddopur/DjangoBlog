# Generated by Django 2.2.11 on 2022-10-20 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0005_auto_20221019_1355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meet',
            old_name='linkdein_profile',
            new_name='linkedin_profile',
        ),
    ]
