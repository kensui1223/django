# Generated by Django 5.0.6 on 2024-06-10 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gakuseikanri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=100)),
                ('student_number', models.CharField(max_length=15)),
                ('student_email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
        migrations.DeleteModel(
            name='Gakuseikanri',
        ),
    ]
