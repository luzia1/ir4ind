# Generated by Django 4.2.3 on 2023-07-20 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_task_metadata_task_metadata_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='metadata_id',
            new_name='metadata',
        ),
    ]