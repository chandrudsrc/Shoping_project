# Generated by Django 4.2.5 on 2023-11-07 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]