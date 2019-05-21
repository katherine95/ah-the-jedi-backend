# Generated by Django 2.2 on 2019-05-14 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fluent_comments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0028_merge_20190509_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('vote_up', models.IntegerField(default=0)),
                ('vote_down', models.IntegerField(default=0)),
                ('comment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comment_id', to='fluent_comments.FluentComment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]