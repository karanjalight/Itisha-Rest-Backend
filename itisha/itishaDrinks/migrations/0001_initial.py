# Generated by Django 4.1.2 on 2022-10-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='itisha_drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_id', models.IntegerField()),
                ('drink_name', models.CharField(max_length=250)),
                ('drink_type', models.CharField(max_length=250)),
                ('drink_qty', models.CharField(max_length=250)),
                ('drink_price', models.IntegerField()),
                ('drink_description', models.CharField(max_length=250)),
                ('shop', models.CharField(max_length=250)),
            ],
        ),
    ]
