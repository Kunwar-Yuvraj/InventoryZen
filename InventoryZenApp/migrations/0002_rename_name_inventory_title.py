# Generated by Django 4.2 on 2024-08-05 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryZenApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='name',
            new_name='title',
        ),
    ]