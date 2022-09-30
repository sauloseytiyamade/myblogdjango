from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class moment(models.Model):
    title = models.CharField(max_length=100)
    photo = CloudinaryField('image')
    text = RichTextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title