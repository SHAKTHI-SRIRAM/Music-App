# Generated by Django 3.1.2 on 2020-10-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('songid', models.CharField(max_length=20)),
                ('artist', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('posteruri', models.CharField(max_length=2086)),
            ],
        ),
    ]