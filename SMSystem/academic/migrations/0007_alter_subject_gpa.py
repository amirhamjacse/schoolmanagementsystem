# Generated by Django 3.2.13 on 2022-08-30 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0006_auto_20220830_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='gpa',
            field=models.CharField(default='n/a', max_length=10),
        ),
    ]