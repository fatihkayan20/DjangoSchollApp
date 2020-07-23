# Generated by Django 3.0.6 on 2020-07-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Başlık')),
                ('content', models.TextField(verbose_name='İçerik')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Zamanı')),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
    ]