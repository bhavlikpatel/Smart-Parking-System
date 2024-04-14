# Generated by Django 4.1.5 on 2023-01-28 03:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parking_app', '0009_fixedslot_carslot_amount_carslot_payment_method_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slottimewindow',
            name='slot',
        ),
        migrations.AddField(
            model_name='fixedslot',
            name='from_time',
            field=models.TimeField(blank=True, null=True, verbose_name='From Time'),
        ),
        migrations.AddField(
            model_name='fixedslot',
            name='sequence_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Slot Number'),
        ),
        migrations.AddField(
            model_name='fixedslot',
            name='slot_date',
            field=models.DateField(default='2023-01-28', verbose_name='Slot Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fixedslot',
            name='to_time',
            field=models.TimeField(blank=True, null=True, verbose_name='To Time'),
        ),
        migrations.AddField(
            model_name='fixedslot',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='slottimewindow',
            name='fixed_slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fixed_slot_windows', to='parking_app.fixedslot'),
        ),
        migrations.AddField(
            model_name='slottimewindow',
            name='user_slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_slot_windows', to='parking_app.carslot'),
        ),
    ]
