# Generated by Django 4.2.2 on 2023-06-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.TextField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('desc', models.CharField(max_length=250)),
            ],
        ),
    ]
