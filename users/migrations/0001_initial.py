# Generated by Django 4.2.4 on 2023-08-12 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsersDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_models', models.CharField(max_length=200)),
                ('password_models', models.CharField(max_length=200)),
            ],
        ),
    ]