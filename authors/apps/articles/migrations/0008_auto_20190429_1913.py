# Generated by Django 2.1 on 2019-04-29 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20190429_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
