# Generated by Django 2.2.21 on 2021-05-12 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Categorie'),
            preserve_default=False,
        ),
    ]
