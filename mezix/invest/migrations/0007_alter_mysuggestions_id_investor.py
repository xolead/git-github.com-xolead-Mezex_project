# Generated by Django 5.0.4 on 2024-05-11 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0006_remove_mysuggestions_id_requestinvestor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysuggestions',
            name='id_Investor',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='invest.investor'),
            preserve_default=False,
        ),
    ]