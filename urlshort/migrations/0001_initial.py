# Generated by Django 4.1.4 on 2022-12-30 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(max_length=700)),
                ('shrt_url', models.CharField(max_length=100)),
                ('TD', models.DateTimeField()),
            ],
        ),
    ]
