# Generated by Django 5.1.4 on 2025-01-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_kyc_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='receipt',
            field=models.FileField(blank=True, help_text='This is the receipt of account payment confirmation.', null=True, upload_to='identity/proof'),
        ),
    ]
