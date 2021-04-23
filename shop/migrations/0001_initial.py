# Generated by Django 3.2 on 2021-04-23 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=15)),
                ('in_box', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.BigIntegerField()),
                ('retail_price', models.BigIntegerField(default=999999)),
                ('description', models.TextField(max_length=10000)),
                ('pic', models.CharField(default='https://i.ytimg.com/vi/83aci6jpngM/maxresdefault.jpg', max_length=100)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]