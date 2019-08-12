# Generated by Django 2.2.3 on 2019-07-30 13:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0002_employee_is_resource'),
        ('organization', '0005_auto_20190726_1935'),
        ('engagement', '0003_auto_20190730_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('planned_start_date', models.DateField(blank=True, null=True)),
                ('actual_start_date', models.DateField(blank=True, null=True)),
                ('planned_end_date', models.DateField(blank=True, null=True)),
                ('actual_end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('not started', 'not started'), ('running', 'running'), ('in review', 'in review'), ('reviewed', 'reviewed'), ('closed', 'closed')], max_length=20)),
                ('engagement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='engagement.Engagement')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager_jobs', to='employee.Employee')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.Organization')),
            ],
            options={
                'db_table': 'job',
            },
        ),
    ]