# Generated by Django 5.1.6 on 2025-03-28 07:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdeskapp', '0002_alter_ticket_options_alter_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='assigned_technician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]
