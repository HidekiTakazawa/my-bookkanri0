# Generated by Django 2.2.5 on 2019-10-06 00:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookkanri', '0005_auto_20191006_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdata',
            name='purchase_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]