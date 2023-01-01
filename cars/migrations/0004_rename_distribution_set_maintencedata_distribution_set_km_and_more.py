# Generated by Django 4.1.4 on 2022-12-31 23:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_year_maintencedata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintencedata',
            old_name='distribution_set',
            new_name='distribution_set_km',
        ),
        migrations.RenameField(
            model_name='maintencedata',
            old_name='oil_change',
            new_name='next_distribution_set_km',
        ),
        migrations.AddField(
            model_name='maintencedata',
            name='distribution_set_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maintencedata',
            name='next_oil_change_km',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maintencedata',
            name='oil_change_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maintencedata',
            name='oil_change_km',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]