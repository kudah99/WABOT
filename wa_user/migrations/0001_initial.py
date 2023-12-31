# Generated by Django 4.2.2 on 2023-06-26 23:53

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WAUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(editable=False, max_length=30, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('IsRegistered', models.BooleanField(default=False)),
                ('IsBlocked', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tbl_wa_users',
            },
            managers=[
                ('my_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
