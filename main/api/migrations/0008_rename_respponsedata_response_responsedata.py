# Generated by Django 4.1.3 on 2023-01-30 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_serivcelocation_response_servicelocation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='respponsedata',
            new_name='responsedata',
        ),
    ]