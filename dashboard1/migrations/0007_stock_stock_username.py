# Generated by Django 3.0.2 on 2020-03-19 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard1', '0006_auto_20200318_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stock_username',
            field=models.CharField(default='', max_length=60),
        ),
    ]
