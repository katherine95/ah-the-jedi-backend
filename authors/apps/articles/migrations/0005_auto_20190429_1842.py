# Generated by Django 2.1 on 2019-04-29 18:42

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190429_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='author',
            field=jsonfield.fields.JSONField(),
        ),
    ]
