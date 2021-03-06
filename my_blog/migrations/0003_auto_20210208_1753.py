# Generated by Django 3.1 on 2021-02-08 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_blog', '0002_blogcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='slug',
            field=models.SlugField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='BlogPost', to=settings.AUTH_USER_MODEL),
        ),
    ]
