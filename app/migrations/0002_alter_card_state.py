# Generated by Django 4.2.9 on 2024-11-25 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='state',
            field=models.CharField(blank=True, choices=[('Created', 'Created'), ('Connected', 'Connected')], max_length=200, null=True),
        ),
    ]
