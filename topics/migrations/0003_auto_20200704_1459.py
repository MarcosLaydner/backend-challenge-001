# Generated by Django 3.0.7 on 2020-07-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_auto_20200704_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='url_name',
            field=models.SlugField(default='', max_length=24),
        ),
    ]
