# Generated by Django 3.2.4 on 2021-06-30 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_userlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
