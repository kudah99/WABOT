# Generated by Django 4.0.7 on 2022-10-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_menu', '0002_delete_mainmenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_en', models.CharField(max_length=300)),
                ('feature_sh', models.CharField(max_length=300)),
                ('feature_nd', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=30)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
