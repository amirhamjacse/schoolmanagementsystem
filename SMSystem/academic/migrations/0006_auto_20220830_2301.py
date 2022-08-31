# Generated by Django 3.2.13 on 2022-08-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0005_auto_20220830_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='gpa',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_name_1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_name_2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_name_3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_number1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_number2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_number3',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]