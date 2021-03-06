from django.db import models
from django.contrib.auth.models import User
from PIL import Image


neighborhood = (
        ('1', 'Red Ville'),
        ('2', 'Green View'),
        ('3', 'The Park'),
        ('4', 'Lil Arcade'),
        ('5', 'Komo Avenue'),)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    neighborhood = models.CharField(max_length=25,choices=neighborhood, default='Red Ville')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

     

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
