from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
import cloudinary.uploader
from django.dispatch import receiver
from django.shortcuts import reverse

CATEGORIES = (
    ('A', 'animal'),
    ('C', 'crop')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    category = models.CharField(choices=CATEGORIES, max_length=1)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()


    def __str__(self):
        return f"{self.title}==================================>>>{self.date_created}"

    def get_absolute_url(self):
        return reverse('core:product', kwargs={
            'slug': self.slug
        })


@receiver(pre_delete, sender=Item)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)
