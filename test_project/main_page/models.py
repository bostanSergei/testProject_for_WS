from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slider_images')

    def __str__(self):
        return f'Изображение для слайдера: {self.title}'
