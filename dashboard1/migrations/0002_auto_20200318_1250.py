# Generated by Django 3.0.2 on 2020-03-18 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stock_catagory',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock_empty',
            field=models.IntegerField(default=0),
        ),
    ]
