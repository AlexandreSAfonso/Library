# Generated by Django 5.1.7 on 2025-03-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=64)),
            ],
        ),
    ]
