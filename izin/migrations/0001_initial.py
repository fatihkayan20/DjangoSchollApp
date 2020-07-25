# Generated by Django 2.1.15 on 2020-07-25 13:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Başlık')),
                ('content', models.TextField(verbose_name='İçerik')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Zamanı')),
                ('event_start_date', models.DateTimeField(verbose_name='Etkinlik Başlangıcı')),
                ('event_end_date', models.DateTimeField(verbose_name='Etkinlik Bitisi')),
                ('slug', models.SlugField(max_length=100)),
                ('accept', models.ManyToManyField(related_name='accept', to=settings.AUTH_USER_MODEL, verbose_name='Kabul')),
                ('veto', models.ManyToManyField(related_name='veto', to=settings.AUTH_USER_MODEL, verbose_name='Red')),
            ],
        ),
    ]
