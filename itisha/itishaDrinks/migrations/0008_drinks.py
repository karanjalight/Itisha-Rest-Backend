# Generated by Django 4.1.2 on 2022-11-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itishaDrinks', '0007_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_id', models.IntegerField()),
                ('drink_type', models.CharField(max_length=250)),
                ('drink_name', models.CharField(max_length=250)),
                ('drink_qty', models.CharField(max_length=250)),
                ('drink_price', models.IntegerField()),
                ('drink_description', models.CharField(max_length=250)),
                ('top_rated', models.BooleanField(default=False, help_text='clicked means it is categorised here')),
                ('recommended', models.BooleanField(default=False, help_text='clicked means it is categorised here')),
                ('offers', models.BooleanField(default=False, help_text='clicked means it is categorised as 15% off')),
            ],
        ),
    ]
