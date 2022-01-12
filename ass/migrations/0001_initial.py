# Generated by Django 4.0 on 2022-01-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=60)),
                ('bio', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
