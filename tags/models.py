from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # To define generic relationship we need the following:
    # FK for the a generic object (can be used in different apps)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # For the object id
    object_id = models.PositiveIntegerField()
    # To get the actual object content from a class from other app
    content_object = GenericForeignKey()
