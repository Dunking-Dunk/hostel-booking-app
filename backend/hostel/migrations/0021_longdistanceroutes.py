# Generated by Django 5.1.7 on 2025-07-25 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0020_roombooking_is_payment_link_sent'),
    ]

    operations = [
        migrations.CreateModel(
            name='LongDistanceRoutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bus Route No.', models.CharField(max_length=10)),
                ('Bus Route Name', models.CharField(max_length=255)),
            ],
        ),
    ]
