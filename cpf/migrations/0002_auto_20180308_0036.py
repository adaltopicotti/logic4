# Generated by Django 2.0.3 on 2018-03-08 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoafisica',
            name='genero',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='mae',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pessoafisica',
            name='situacao',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
