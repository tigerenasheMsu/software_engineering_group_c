# Generated by Django 4.0.2 on 2022-02-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters_registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotersRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15)),
                ('surname', models.CharField(max_length=15)),
                ('id_number', models.CharField(max_length=13)),
                ('address', models.TextField(max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('timestamp', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
