# Generated by Django 4.2.2 on 2023-07-05 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_technology'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='discription',
        ),
    ]