# Generated by Django 4.1.5 on 2023-02-03 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0016_remove_fixedslot_from_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='vehicle_type',
            field=models.CharField(choices=[('TWO_WHEELER', '2 Wheeler'), ('THREE_WHEELER', '3 Wheeler'), ('FOUR_WHEELER', '4 wheeler'), ('SIX_WHEELER', '6 wheeler'), ('EIGHT_WHEELER', '8 wheeler'), ('OTHER', 'Other')], default='FOUR_WHEELER', max_length=30, verbose_name='Vehicle Type'),
        ),
    ]
