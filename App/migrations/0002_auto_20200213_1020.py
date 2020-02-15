# Generated by Django 2.2.5 on 2020-02-13 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'get_latest_by': ['id']},
        ),
        migrations.AlterField(
            model_name='record',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
