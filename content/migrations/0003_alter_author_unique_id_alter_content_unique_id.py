# Generated by Django 5.0.1 on 2024-02-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_author_data_alter_content_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='unique_id',
            field=models.IntegerField(db_index=True, unique=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='unique_id',
            field=models.IntegerField(db_index=True, unique=True),
        ),
    ]
