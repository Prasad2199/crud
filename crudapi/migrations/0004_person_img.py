# Generated by Django 4.0.2 on 2022-02-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapi', '0003_remove_person_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='img',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/%y/%m/%d/'),
        ),
    ]
