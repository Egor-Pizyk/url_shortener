# Generated by Django 4.1.2 on 2022-10-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shortener", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="url",
            name="counter",
            field=models.IntegerField(default=0),
        ),
    ]
