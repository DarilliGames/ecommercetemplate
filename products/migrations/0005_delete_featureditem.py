# Generated by Django 3.2.6 on 2021-08-20 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_catagory_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FeaturedItem',
        ),
    ]
