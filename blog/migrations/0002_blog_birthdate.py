# Generated by Django 4.2.2 on 2023-07-03 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]