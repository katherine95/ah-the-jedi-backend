# Generated by Django 2.1 on 2019-05-02 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_auto_20190501_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='linkedIn',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='mail',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]
