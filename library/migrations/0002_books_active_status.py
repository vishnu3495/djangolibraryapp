# Generated by Django 4.0.4 on 2022-06-29 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='active_status',
            field=models.BooleanField(default=True),
        ),
    ]
