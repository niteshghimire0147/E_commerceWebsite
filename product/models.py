
from random import choice, choices
from django.db import models

images_choices = [
    ('carousel_image', 'carousel_image'),
    ('collection_image', 'collection_image'),
    ('discount_banner', 'discount_banner'),
    ('discount_time_banner', 'discount_time_banner'),
]
# Create your models here.



class top_slider(models.Model):
    name = models.CharField(max_length=5000,choices=images_choices)
    image = models.ImageField(upload_to='media', null=True)

    def __str__(self):
        return f'{self.image}'







    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)

    #     if img.height != 510 or img.width != 1900:
    #         output_size = (510,1900)
    #         img.thumbnail(output_size)
    #         img.save(self.image)
                

