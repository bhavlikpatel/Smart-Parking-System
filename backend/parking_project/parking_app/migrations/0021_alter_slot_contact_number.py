# Generated by Django 4.0.1 on 2024-03-12 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0020_rename_slot_slot_fixed_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='contact_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Contact Number'),
        ),
    ]
