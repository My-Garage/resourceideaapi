# Generated by Django 2.2.5 on 2019-09-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='src_client_id',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]