# Generated by Django 4.2 on 2025-05-16 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_requests', '0002_rendezvous_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='demande',
            new_name='service_request',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='related_demande',
            new_name='related_service_request',
        ),
    ]
