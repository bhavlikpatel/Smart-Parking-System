# Generated by Django 4.1.5 on 2023-02-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0014_slot_reference_number_slot_vehicle_plat_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='contact_number',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Contact Number'),
        ),
    ]