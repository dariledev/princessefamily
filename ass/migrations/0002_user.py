# Generated by Django 4.0 on 2022-01-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]
