# Generated by Django 4.0.5 on 2022-06-14 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employees_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='full_name',
            new_name='name',
        ),
    ]
