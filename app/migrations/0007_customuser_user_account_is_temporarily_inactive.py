# Generated by Django 4.2.9 on 2024-12-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_customuser_user_account_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_account_is_temporarily_inactive',
            field=models.BooleanField(default=False),
        ),
    ]
