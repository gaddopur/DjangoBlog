# Generated by Django 2.2.11 on 2020-07-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200706_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecomment',
            name='child',
            field=models.ManyToManyField(blank=True, null=True, related_name='_articlecomment_child_+', to='articles.ArticleComment'),
        ),
    ]