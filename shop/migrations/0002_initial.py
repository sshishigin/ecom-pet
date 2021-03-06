# Generated by Django 3.2.3 on 2021-06-23 12:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useritemrelation',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.category'),
        ),
        migrations.AddField(
            model_name='item',
            name='users',
            field=models.ManyToManyField(through='shop.UserItemRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]
