# Generated by Django 4.0.2 on 2022-02-06 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapi', '0002_alter_person_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='img',
        ),
    ]
