# Generated by Django 4.1.2 on 2022-11-03 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_designer_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='designer',
            old_name='id',
            new_name='des_id',
        ),
        migrations.RenameField(
            model_name='designer',
            old_name='name',
            new_name='des_name',
        ),
        migrations.RenameField(
            model_name='designer',
            old_name='password',
            new_name='des_password',
        ),
    ]
