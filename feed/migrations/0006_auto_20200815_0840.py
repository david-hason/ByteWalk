# Generated by Django 3.0.8 on 2020-08-15 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20200814_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
