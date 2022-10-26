# Generated by Django 4.1.2 on 2022-10-26 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('itishaDrinks', '0006_delete_itisha_drinks'),
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
                ('shops', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itishaDrinks.drink_shop')),
            ],
        ),
    ]
