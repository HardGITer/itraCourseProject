# Generated by Django 2.1.1 on 2018-10-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseProject', '0010_auto_20181005_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='CourseProject.Tag'),
        ),
    ]
