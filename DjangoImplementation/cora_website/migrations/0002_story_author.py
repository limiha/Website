# Generated by Django 3.0.5 on 2020-04-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cora_website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='author',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
    ]