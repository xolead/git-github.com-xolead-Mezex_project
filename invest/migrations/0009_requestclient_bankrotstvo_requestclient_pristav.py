# Generated by Django 5.0.4 on 2024-05-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0008_alter_mysuggestions_specialconditions'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestclient',
            name='bankrotstvo',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requestclient',
            name='pristav',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
