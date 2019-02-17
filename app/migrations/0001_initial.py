# Generated by Django 2.1.7 on 2019-02-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WineCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('country', models.CharField(default=None, max_length=100)),
                ('description', models.TextField(default=None, max_length=4000)),
                ('designation', models.TextField(default=None, max_length=4000)),
                ('points', models.IntegerField(default=None)),
                ('price', models.IntegerField(default=None)),
                ('province', models.CharField(default=None, max_length=100)),
                ('region_1', models.CharField(default=None, max_length=100)),
                ('region_2', models.CharField(default=None, max_length=100)),
                ('variety', models.CharField(default=None, max_length=100)),
                ('winery', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]
