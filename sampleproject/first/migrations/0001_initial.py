# Generated by Django 4.2.1 on 2023-06-05 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
