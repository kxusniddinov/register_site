# Generated by Django 5.1.6 on 2025-02-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=200)),
                ('company', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250)),
                ('exist', models.CharField(max_length=3)),
            ],
        ),
    ]
