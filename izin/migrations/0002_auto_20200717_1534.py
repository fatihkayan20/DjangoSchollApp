# Generated by Django 3.0.6 on 2020-07-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='slug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='permission',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Başlık'),
        ),
    ]
