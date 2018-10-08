from django.db.models.signals import post_save
from django.dispatch import receiver

from CourseProject.models import Article


@receiver(post_save, sender=Article)
def index_post(sender, instance, **kwargs):
    instance.indexing()