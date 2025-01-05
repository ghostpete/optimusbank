# Generated by Django 5.1.4 on 2025-01-05 14:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_transfer_iban_code_alter_account_bank_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder_name', models.CharField(blank=True, max_length=200, null=True)),
                ('account_number', models.CharField(blank=True, max_length=200, null=True)),
                ('ach_routing', models.CharField(blank=True, max_length=200, null=True)),
                ('iban_code', models.CharField(blank=True, max_length=300, null=True)),
                ('account_type', models.CharField(blank=True, choices=[('CHECKING', 'CHECKING'), ('SAVINGS', 'SAVINGS'), ('MONEY MARKET', 'MONEY MARKET'), ('PLATINUM', 'PLATINUM')], max_length=200, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('from_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfered_details_from', to='app.account')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transfer',
                'verbose_name_plural': 'Transfer',
            },
        ),
    ]