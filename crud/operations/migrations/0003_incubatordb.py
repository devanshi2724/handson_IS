# Generated by Django 4.2.1 on 2023-05-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncubatorDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_desc', models.TextField()),
                ('no_of_employees', models.IntegerField()),
                ('components', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=30)),
                ('user_id', models.IntegerField()),
                ('customer_count', models.CharField(max_length=30)),
                ('sti_owner', models.CharField(max_length=50)),
                ('revenue', models.IntegerField(blank=True, null=True)),
                ('effort_involved', models.IntegerField()),
                ('no_of_customer', models.IntegerField()),
                ('is_new_business', models.BooleanField(blank=True, default=False, null=True)),
                ('creation_date', models.DateField()),
                ('ideation_count', models.IntegerField(default=0)),
                ('incubation_count', models.IntegerField(default=0)),
                ('scaling_count', models.IntegerField(default=0)),
                ('industrialized_count', models.IntegerField(default=0)),
                ('optimised_count', models.IntegerField(default=0)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
