# Generated by Django 5.0.4 on 2024-05-11 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0007_alter_mysuggestions_id_investor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysuggestions',
            name='SpecialConditions',
            field=models.TextField(null=True),
        ),
    ]