# Generated by Django 4.0.4 on 2022-04-29 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_5', '0004_alter_flower_delivered_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='diname',
            new_name='name',
        ),
    ]
