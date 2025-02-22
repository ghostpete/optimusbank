# Generated by Django 5.1.4 on 2025-01-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_account_ssn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transferdetails',
            old_name='address',
            new_name='beneficiary_name',
        ),
        migrations.AddField(
            model_name='transferdetails',
            name='location',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='transferdetails',
            name='account_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
