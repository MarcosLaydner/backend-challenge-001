# Generated by Django 3.0.7 on 2020-07-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_auto_20200705_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='url_name',
            field=models.SlugField(default='', max_length=24, unique=True),
        ),
    ]
