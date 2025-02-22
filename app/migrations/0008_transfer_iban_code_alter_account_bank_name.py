# Generated by Django 5.1.4 on 2025-01-05 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_customuser_user_account_is_temporarily_inactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='iban_code',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='bank_name',
            field=models.CharField(blank=True, default='Optimum Bank', max_length=200, null=True),
        ),
    ]
