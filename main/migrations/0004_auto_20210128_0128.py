# Generated by Django 3.1.3 on 2021-01-27 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210125_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=20),
        ),
    ]
