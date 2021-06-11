# Generated by Django 3.2.3 on 2021-05-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('C', 'Cookies,Deserts'), ('V', 'Vegetables,Fruits'), ('D', 'Soft,Energy Drinks'), ('F', 'Fast Foods')], max_length=2),
        ),
    ]
