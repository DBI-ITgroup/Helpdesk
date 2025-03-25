# Generated by Django 5.1.6 on 2025-03-25 08:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('ticket_number', models.CharField(blank=True, max_length=20, unique=True)),
                ('ticket_title', models.CharField(max_length=255)),
                ('department', models.CharField(choices=[('IT', 'IT'), ('HR', 'HR'), ('Finance', 'Finance')], max_length=100)),
                ('contact_info', models.CharField(max_length=255)),
                ('problem_description', models.TextField()),
                ('priority_level', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=50)),
                ('preferred_contact_method', models.CharField(choices=[('Email', 'Email'), ('Phone', 'Phone')], max_length=50)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('date_created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
