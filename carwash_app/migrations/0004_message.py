# Generated by Django 4.0.4 on 2022-04-20 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash_app', '0003_pay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.TextField(max_length=190)),
                ('Email', models.TextField(max_length=190)),
                ('Select_service', models.TextField(max_length=190)),
                ('Requirements', models.TextField(max_length=190)),
            ],
        ),
    ]
