# Generated by Django 3.2.4 on 2021-07-05 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pic',
            field=models.CharField(default='https://images.pexels.com/photos/1666067/pexels-photo-1666067.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260', max_length=130),
        ),
    ]