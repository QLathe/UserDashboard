# Generated by Django 2.2.4 on 2021-01-29 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='messafe',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
