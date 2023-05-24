# Generated by Django 4.2.1 on 2023-05-15 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]