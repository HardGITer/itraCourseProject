# Generated by Django 2.1.1 on 2018-10-05 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CourseProject', '0006_remove_tag_article'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='TagForArticle',
        ),
    ]
