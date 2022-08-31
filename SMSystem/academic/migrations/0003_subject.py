# Generated by Django 3.2.13 on 2022-08-30 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_alter_student_cgpa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.CharField(max_length=10)),
                ('std', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.student')),
            ],
        ),
    ]