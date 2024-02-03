# Generated by Django 5.0.1 on 2024-02-03 05:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.IntegerField()),
                ('username', models.CharField(max_length=255)),
                ('data', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.IntegerField(unique=True)),
                ('data', models.JSONField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.author')),
            ],
        ),
    ]
