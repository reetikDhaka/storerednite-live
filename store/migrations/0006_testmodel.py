# Generated by Django 3.2.4 on 2021-06-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='testModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('likes', models.IntegerField()),
            ],
        ),
    ]
