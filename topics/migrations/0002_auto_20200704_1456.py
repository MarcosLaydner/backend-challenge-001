# Generated by Django 3.0.7 on 2020-07-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
