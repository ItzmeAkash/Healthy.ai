# Generated by Django 4.2.10 on 2024-02-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietrecommendation',
            name='physical_activity',
            field=models.CharField(choices=[('1', 'Sedentray'), ('2', 'LightlyActive'), ('3', 'ModeratelyActive'), ('4', 'ExtremelyActive')], max_length=1),
        ),
    ]
