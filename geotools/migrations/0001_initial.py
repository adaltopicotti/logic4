# Generated by Django 2.0.3 on 2018-03-22 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat_deg', models.IntegerField()),
                ('lat_min', models.IntegerField()),
                ('lat_sec', models.FloatField()),
                ('lon_deg', models.IntegerField()),
                ('lon_min', models.IntegerField()),
                ('lon_sec', models.FloatField()),
            ],
        ),
    ]
