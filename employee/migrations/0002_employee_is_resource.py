# Generated by Django 2.2.3 on 2019-07-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_resource',
            field=models.BooleanField(default=False),
        ),
    ]