# Generated by Django 4.2 on 2024-02-16 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0004_alter_dietrecommendation_goal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodimagemodel',
            name='username',
        ),
    ]
