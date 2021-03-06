# Generated by Django 4.0.3 on 2022-03-12 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_mobile', models.BigIntegerField()),
                ('user_email', models.EmailField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('con_pwd', models.CharField(max_length=100)),
                ('status', models.CharField(default='pending', max_length=100, null=True)),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
    ]
