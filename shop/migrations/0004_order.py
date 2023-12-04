# Generated by Django 4.2.5 on 2023-11-06 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_favourite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mbl', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=7, null=True)),
                ('address', models.CharField(max_length=15, null=True)),
                ('feedback', models.TextField(max_length=40)),
            ],
        ),
    ]
