# Generated by Django 2.2.11 on 2020-07-01 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200618_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='accounts/images/default_profile.jpg', upload_to='accounts/images'),
        ),
    ]
