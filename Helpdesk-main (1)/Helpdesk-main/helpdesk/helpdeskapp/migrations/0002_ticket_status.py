# Generated by Django 5.1.6 on 2025-03-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdeskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
