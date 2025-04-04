# Generated by Django 5.1.6 on 2025-03-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdeskapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'permissions': [('view_pending_tickets', 'Can view pending tickets'), ('view_completed_tickets', 'Can view completed tickets')]},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('End-User', 'End-User'), ('Technician', 'Technician'), ('Administrator', 'Administrator'), ('L1_Technician', 'L1_Technician'), ('L2_Technician', 'L2_Technician'), ('CAB', 'CAB')], max_length=20),
        ),
    ]
