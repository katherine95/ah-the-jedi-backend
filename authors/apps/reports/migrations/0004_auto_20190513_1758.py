# Generated by Django 2.2 on 2019-05-13 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20190513_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportmodel',
            old_name='user',
            new_name='reporter',
        ),
    ]