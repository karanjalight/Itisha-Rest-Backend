# Generated by Django 4.1.2 on 2022-10-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itishaDrinks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='drink_shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.IntegerField()),
                ('shop_name', models.CharField(max_length=50)),
                ('shop_location', models.CharField(max_length=50)),
                ('shop_owner', models.CharField(max_length=50)),
                ('shop_contacts', models.CharField(max_length=10)),
            ],
        ),
    ]
