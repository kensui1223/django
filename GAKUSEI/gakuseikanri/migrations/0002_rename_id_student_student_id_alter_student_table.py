# Generated by Django 5.0.4 on 2024-06-09 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gakuseikanri', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='id',
            new_name='student_id',
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]