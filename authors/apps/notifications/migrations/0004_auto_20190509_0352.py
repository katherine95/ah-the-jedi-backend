# Generated by Django 2.1 on 2019-05-09 03:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0003_auto_20190509_0350'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Unsubscriptions',
            new_name='Subscriptions',
        ),
    ]