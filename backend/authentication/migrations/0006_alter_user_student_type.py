# Generated by Django 5.1.7 on 2025-04-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_user_student_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_type',
            field=models.CharField(choices=[('Mgmt', 'Management'), ('Govt', 'Govt')], default='Mgmt', max_length=10),
        ),
    ]
