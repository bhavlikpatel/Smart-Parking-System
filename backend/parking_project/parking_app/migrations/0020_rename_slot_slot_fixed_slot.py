# Generated by Django 4.1.5 on 2023-02-11 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0019_remove_slot_sequence_number_remove_slot_slot_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slot',
            old_name='slot',
            new_name='fixed_slot',
        ),
    ]