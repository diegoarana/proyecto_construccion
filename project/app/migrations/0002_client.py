# Generated by Django 2.0.5 on 2018-05-26 22:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('phone', models.PositiveIntegerField(help_text='(Solamente dígitos)', validators=[django.core.validators.MaxValueValidator(999999999999999)])),
            ],
        ),
    ]
