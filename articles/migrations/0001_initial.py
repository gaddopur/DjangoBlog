# Generated by Django 2.2.11 on 2020-07-06 01:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('thumb', models.ImageField(blank=True, default='articles/images/default.jfif', upload_to='articles/images')),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('height', models.IntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='articles.ArticleComment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['tree_id', 'lft'],
            },
        ),
    ]
