# Generated by Django 4.2.9 on 2024-12-06 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_payment_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_account_is_active',
            field=models.BooleanField(default=True),
        ),
    ]
