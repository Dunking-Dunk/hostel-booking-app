# Generated by Django 5.1.7 on 2025-04-11 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_tution_fee'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('dept', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='tution_fee',
            field=models.BooleanField(default=True),
        ),
    ]
