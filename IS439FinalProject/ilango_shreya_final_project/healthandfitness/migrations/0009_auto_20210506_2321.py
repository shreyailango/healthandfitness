# Generated by Django 3.1.7 on 2021-05-06 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthandfitness', '0008_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
