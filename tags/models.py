from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class TaggedItemManager(models.Model):
    def get_tags_for(self, object_type, object_id):
        content_type = ContentType.objects.get_for_model(object_type)

        return TaggedItem.objects.select_related('tag').filter(content_type=content_type, object_id=object_id)



class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    objects = TaggedItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # To define generic relationship we need the following:
    # FK for the a generic object (can be used in different apps)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # For the object id
    object_id = models.PositiveIntegerField()
    # To get the actual object content from a class from other app
    content_object = GenericForeignKey()
