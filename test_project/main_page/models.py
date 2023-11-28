from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=255)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, editable=True)
    image = models.ImageField(upload_to='slider_images')

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f'Изображение для слайдера: {self.title}'
