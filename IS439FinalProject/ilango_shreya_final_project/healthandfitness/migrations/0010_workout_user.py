# Generated by Django 3.1.7 on 2021-05-06 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthandfitness', '0009_auto_20210506_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='user',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
