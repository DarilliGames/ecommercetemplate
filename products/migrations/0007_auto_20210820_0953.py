# Generated by Django 3.2.6 on 2021-08-20 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_content_product_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catagory',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='catagory',
            new_name='category',
        ),
    ]