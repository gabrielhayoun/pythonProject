# Generated by Django 2.2.21 on 2021-05-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210512_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]