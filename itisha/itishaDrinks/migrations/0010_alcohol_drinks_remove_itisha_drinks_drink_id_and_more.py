# Generated by Django 4.1.2 on 2022-11-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itishaDrinks', '0009_delete_drinks_remove_itisha_drinks_shops_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='alcohol_drinks',
            fields=[
                ('drink_slug', models.CharField(help_text='the names of the product SHOULD be unique to every product.', max_length=250, primary_key=True, serialize=False)),
                ('drink_type', models.CharField(help_text='this is the drink category, either alcohol, Energy drink, juice ...', max_length=250)),
                ('drink_name', models.CharField(help_text='Can be same to drink slug, (but not every time)', max_length=250)),
                ('drink_qty', models.CharField(max_length=250)),
                ('drink_price', models.IntegerField()),
                ('alcohol_drinks_type', models.CharField(choices=[('', 'Gin'), ('W', 'Whiskey'), ('V', 'Vodka')], max_length=20)),
                ('drink_description', models.CharField(max_length=250)),
                ('top_rated', models.BooleanField(default=False, help_text='categorised under the top rated category')),
                ('recommended', models.BooleanField(default=False, help_text=' recommencded to other users')),
                ('offers', models.BooleanField(default=False, help_text=' categorised as 15% off')),
            ],
        ),
        migrations.RemoveField(
            model_name='itisha_drinks',
            name='drink_id',
        ),
        migrations.RemoveField(
            model_name='itisha_drinks',
            name='id',
        ),
        migrations.AddField(
            model_name='itisha_drinks',
            name='drink_slug',
            field=models.CharField(default=1, help_text='the names of the product SHOULD be unique to every product.', max_length=250, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itisha_drinks',
            name='drink_name',
            field=models.CharField(help_text='Can be same to drink slug, (but not every time)', max_length=250),
        ),
        migrations.AlterField(
            model_name='itisha_drinks',
            name='drink_type',
            field=models.CharField(help_text='this is the drink category, either alcohol, Energy drink, juice ...', max_length=250),
        ),
        migrations.AlterField(
            model_name='itisha_drinks',
            name='offers',
            field=models.BooleanField(default=False, help_text=' categorised as 15% off'),
        ),
        migrations.AlterField(
            model_name='itisha_drinks',
            name='recommended',
            field=models.BooleanField(default=False, help_text=' recommencded to other users'),
        ),
        migrations.AlterField(
            model_name='itisha_drinks',
            name='top_rated',
            field=models.BooleanField(default=False, help_text='categorised under the top rated category'),
        ),
    ]
