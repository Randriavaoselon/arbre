# Generated by Django 3.2.8 on 2022-03-14 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('individu', '0015_remove_individu_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='individu',
            name='age',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
