# Generated by Django 5.0.6 on 2024-06-27 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='musician.musician')),
            ],
        ),
    ]