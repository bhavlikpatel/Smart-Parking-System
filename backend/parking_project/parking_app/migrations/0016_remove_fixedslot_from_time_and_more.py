# Generated by Django 4.1.5 on 2023-02-03 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0015_slot_contact_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixedslot',
            name='from_time',
        ),
        migrations.RemoveField(
            model_name='fixedslot',
            name='is_booked',
        ),
        migrations.RemoveField(
            model_name='fixedslot',
            name='sequence_number',
        ),
        migrations.RemoveField(
            model_name='fixedslot',
            name='slot_date',
        ),
        migrations.RemoveField(
            model_name='fixedslot',
            name='to_time',
        ),
        migrations.RemoveField(
            model_name='fixedslot',
            name='user',
        ),
    ]
