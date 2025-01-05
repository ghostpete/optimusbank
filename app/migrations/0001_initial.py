# Generated by Django 4.2.9 on 2024-11-22 16:09

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('can_apply_for_loans', models.BooleanField(default=False)),
                ('can_apply_for_account', models.BooleanField(default=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced')], max_length=100, null=True)),
                ('number_of_dependents', models.IntegerField(blank=True, null=True)),
                ('otp_code', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('ssn', models.CharField(blank=True, max_length=500, null=True)),
                ('tax_identity_number', models.CharField(blank=True, max_length=500, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('bank_id', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('preferred_account_type', models.CharField(blank=True, choices=[('CHECKING', 'Checking'), ('SAVINGS', 'SAVINGS'), ('MONEY MARKET', 'MONEY MARKET'), ('CD', 'Certificate of Deposit (CD)')], max_length=100, null=True)),
                ('profile_image', models.FileField(blank=True, null=True, upload_to='profile/images')),
                ('employment_status', models.CharField(blank=True, choices=[('Employed', 'Employed'), ('Self-employed', 'Self-employed'), ('Unemployed', 'Unemployed'), ('Retired', 'Retired')], max_length=100, null=True)),
                ('employer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('employer_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('employment_type', models.CharField(blank=True, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('Temporary', 'Temporary')], max_length=200, null=True)),
                ('job_title', models.CharField(blank=True, max_length=200, null=True)),
                ('job_start_date', models.DateField(blank=True, null=True)),
                ('job_end_date', models.DateField(blank=True, null=True)),
                ('annual_income', models.CharField(blank=True, max_length=300, null=True)),
                ('proof_of_employment', models.FileField(blank=True, null=True, upload_to='identity/proof')),
                ('proof_of_income', models.FileField(blank=True, null=True, upload_to='identity/proof')),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('is_usa_citizen', models.CharField(blank=True, default=False, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=100, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('government_id_type', models.CharField(blank=True, default=[('Driver Licence', 'Driver Licence'), ('National ID', 'National ID'), ('Passport', 'Passport')], max_length=200, null=True)),
                ('government_id_number', models.CharField(blank=True, max_length=200, null=True)),
                ('front_id_image', models.FileField(blank=True, null=True, upload_to='identity/images')),
                ('back_id_image', models.FileField(blank=True, null=True, upload_to='identity/images')),
                ('citizenship_status', models.CharField(choices=[('US Citizen', 'US Citizen'), ('Non-US Citizen', 'Non-US Citizen')], default='Non-US Citizen', max_length=50)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.CharField(max_length=500)),
                ('credit_score', models.IntegerField(blank=True, null=True)),
                ('account_number', models.CharField(default=app.models.generate_account_number, max_length=100, unique=True)),
                ('account_type', models.CharField(choices=[('CHECKING', 'CHECKING'), ('SAVINGS', 'SAVINGS'), ('MONEY MARKET', 'MONEY MARKET'), ('PLATINUM', 'PLATINUM')], max_length=40)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bank_name', models.CharField(blank=True, default='FirstCitzen Bank', max_length=200, null=True)),
                ('location', models.CharField(blank=True, default=app.models.change_account_location, max_length=500, null=True)),
                ('ach_routing', models.CharField(blank=True, default=app.models.generate_ach_routing, max_length=9, null=True)),
                ('employment_status', models.CharField(blank=True, choices=[('Employed', 'Employed'), ('Self-employed', 'Self-employed'), ('Unemployed', 'Unemployed'), ('Retired', 'Retired')], max_length=100, null=True)),
                ('employer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('employer_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('employment_type', models.CharField(blank=True, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('Temporary', 'Temporary')], max_length=200, null=True)),
                ('job_title', models.CharField(blank=True, max_length=200, null=True)),
                ('job_start_date', models.DateField(blank=True, null=True)),
                ('job_end_date', models.DateField(blank=True, null=True)),
                ('annual_income', models.CharField(blank=True, max_length=300, null=True)),
                ('proof_of_employment', models.FileField(blank=True, null=True, upload_to='identity/proof')),
                ('proof_of_income', models.FileField(blank=True, null=True, upload_to='identity/proof')),
                ('address', models.TextField(blank=True, null=True)),
                ('business_address', models.TextField(blank=True, null=True)),
                ('business_address2', models.TextField(blank=True, null=True)),
                ('utility_bill', models.FileField(blank=True, null=True, upload_to='identity/proof/utility')),
                ('government_id_type', models.CharField(blank=True, default=[('Driver Licence', 'Driver Licence'), ('National ID', 'National ID')], max_length=200, null=True)),
                ('government_id_number', models.CharField(blank=True, max_length=200, null=True)),
                ('front_id_image', models.FileField(blank=True, null=True, upload_to='identity/images')),
                ('back_id_image', models.FileField(blank=True, null=True, upload_to='identity/images')),
                ('deposit_amount', models.IntegerField(blank=True, null=True)),
                ('is_joint_account', models.BooleanField(default=False)),
                ('joint_account_holder_first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('joint_account_holder_last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('joint_account_holder_ssn', models.CharField(blank=True, max_length=100, null=True)),
                ('joint_account_holder_address', models.TextField(blank=True, null=True)),
                ('joint_account_holder_email', models.CharField(blank=True, max_length=100, null=True)),
                ('joint_account_holder_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('joint_account_holder_government_id_type', models.CharField(blank=True, max_length=300, null=True)),
                ('joint_account_holder_government_id_number', models.CharField(blank=True, max_length=300, null=True)),
                ('joint_account_holder_front_id_image', models.FileField(blank=True, null=True, upload_to='identity/images')),
                ('joint_account_holder_back_id_image', models.FileField(blank=True, null=True, upload_to='identity/images')),
                ('confirmation_payment_amount', models.IntegerField(default=100)),
                ('activated', models.BooleanField(default=False)),
                ('applied_for_activation', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder_name', models.CharField(blank=True, max_length=200, null=True)),
                ('account_number', models.CharField(blank=True, max_length=200, null=True)),
                ('ach_routing', models.CharField(blank=True, max_length=200, null=True)),
                ('account_type', models.CharField(blank=True, choices=[('CHECKING', 'CHECKING'), ('SAVINGS', 'SAVINGS'), ('MONEY MARKET', 'MONEY MARKET'), ('PLATINUM', 'PLATINUM')], max_length=200, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('from_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfered_from', to='app.account')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transfer',
                'verbose_name_plural': 'Transfer',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('DEPOSIT REQUEST', 'DEPOSIT REQUEST'), ('FUND CARD', 'FUND CARD'), ('WITHDRAWAL', 'WITHDRAWAL'), ('TRANSFER', 'TRANSFER')], max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Successful', 'Successful')], default='Pending', max_length=20)),
                ('from_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_transactions', to='app.account')),
                ('to_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_transactions', to='app.account')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=400)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('image', models.FileField(blank=True, null=True, upload_to='support/images/')),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Fulfilled', 'Fulfilled')], default='Pending', max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Support',
                'verbose_name_plural': 'Support',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(blank=True, choices=[('transfer', 'transfer'), ('withdrawal', 'withdrawal'), ('deposit', 'deposit')], max_length=400)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('confirmation_receipt', models.FileField(blank=True, null=True, upload_to='receipts/')),
                ('payment_method', models.CharField(blank=True, choices=[('bank', 'bank'), ('crypto', 'crypto'), ('paypal', 'paypal'), ('cashapp', 'cashapp')], max_length=400)),
                ('is_tax', models.BooleanField(default=False)),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notifications',
                'verbose_name_plural': 'Notification',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(choices=[('personal', 'Personal Loan'), ('mortgage', 'Mortgage'), ('auto', 'Auto Loan'), ('business', 'Business Loan')], max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('loan_term', models.IntegerField(default=12)),
                ('interest_rate', models.DecimalField(decimal_places=2, default=10.0, max_digits=5)),
                ('interest', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('repayment_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('loan_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
                ('is_paid', models.BooleanField(default=False)),
                ('activation_receipt', models.FileField(blank=True, null=True, upload_to='receipts/')),
                ('activated', models.BooleanField(default=False)),
                ('applied_for_activation', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Loan',
                'verbose_name_plural': 'Loans',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, choices=[('CREATED', 'CREATED'), ('CONNECTED', 'CONNECTED')], max_length=200, null=True)),
                ('card_number', models.CharField(blank=True, max_length=200, null=True)),
                ('card_type', models.CharField(blank=True, max_length=200, null=True)),
                ('card_category', models.CharField(blank=True, max_length=200, null=True)),
                ('cvv', models.CharField(blank=True, max_length=30, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('name_in_card', models.CharField(blank=True, max_length=200, null=True)),
                ('is_real_card', models.BooleanField(default=False)),
                ('month_and_year_of_expiration', models.CharField(blank=True, max_length=100, null=True)),
                ('confirmation_receipt', models.FileField(blank=True, null=True, upload_to='receipts/')),
                ('amount_in_card', models.IntegerField(default=0)),
                ('activated', models.BooleanField(default=False)),
                ('card_activation_fee', models.IntegerField(default=100)),
                ('applied_for_activation', models.BooleanField(default=False)),
                ('card_expiration', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cards', to='app.account')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
    ]