# Generated by Django 4.1.4 on 2023-01-11 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToursApp', '0012_remove_bookingmodel_from_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagemodel',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToursApp.destinationmodel'),
        ),
    ]
