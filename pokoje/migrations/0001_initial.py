# Generated by Django 4.2.4 on 2023-08-12 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokoje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwapokoju', models.CharField(max_length=200)),
                ('wartosc1', models.IntegerField()),
                ('wartosc2', models.IntegerField()),
                ('wartosc3', models.CharField(max_length=200)),
            ],
        ),
    ]
