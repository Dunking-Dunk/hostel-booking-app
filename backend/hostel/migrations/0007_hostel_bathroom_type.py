# Generated by Django 5.1.7 on 2025-04-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0006_paymentmanagement_hostel_first_year_fee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='bathroom_type',
            field=models.CharField(choices=[('Attached', 'Attached'), ('Common', 'Common')], default='Common', max_length=20),
        ),
    ]
