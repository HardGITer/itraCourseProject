# Generated by Django 2.1.1 on 2018-10-05 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CourseProject', '0008_article_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.DeleteModel(
            name='TagForArticle',
        ),
    ]
