# Generated by Django 2.1.1 on 2018-10-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseProject', '0002_article_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
