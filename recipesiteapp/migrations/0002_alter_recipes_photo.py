# Generated by Django 5.0.2 on 2024-02-25 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesiteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='photo',
            field=models.ImageField(default=None, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
