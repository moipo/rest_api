# Generated by Django 4.1.3 on 2023-01-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]