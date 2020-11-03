# Generated by Django 3.1 on 2020-11-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20201103_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='school',
            field=models.CharField(choices=[('', 'Wybierz szkołę'), ('ps', 'Szkoła Podstawowa'), ('ms', 'Szkoła Średnia'), ('cl', 'Studia')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.CharField(choices=[('', 'Wybierz przedmiot'), ('mat', 'Matematyka'), ('fiz', 'Fizyka'), ('inf', 'Informatyka'), ('pol', 'Język Polski'), ('ang', 'Język Angielski'), ('nmc', 'Język Niemiecki'), ('his', 'Historia'), ('bio', 'Biologia'), ('che', 'Chemia'), ('geo', 'Geografia')], default='', max_length=3),
        ),
    ]