# Generated by Django 2.1.1 on 2018-10-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseProject', '0003_auto_20181003_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
