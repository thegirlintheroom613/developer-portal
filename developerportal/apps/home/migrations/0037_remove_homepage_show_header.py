# Generated by Django 2.2.12 on 2020-05-26 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_update_streamblock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='show_header',
        ),
    ]