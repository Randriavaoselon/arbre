# Generated by Django 3.2.8 on 2022-03-15 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('individu', '0016_individu_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individu',
            name='id_ep',
            field=models.IntegerField(null=True),
        ),
    ]
