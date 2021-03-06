# Generated by Django 4.0.3 on 2022-03-12 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaptainRegistrationModel',
            fields=[
                ('captain_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('mobile_no', models.BigIntegerField(max_length=15)),
                ('email_address', models.EmailField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('con_password', models.CharField(max_length=100)),
                ('status', models.CharField(default='pending', max_length=100, null=True)),
            ],
            options={
                'db_table': 'captain_reg_details',
            },
        ),
    ]
