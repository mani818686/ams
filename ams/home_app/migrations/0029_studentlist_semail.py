# Generated by Django 3.0.6 on 2020-06-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0028_auto_20200609_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentlist',
            name='semail',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
