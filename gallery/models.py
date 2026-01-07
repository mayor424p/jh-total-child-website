from django.db import models

class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('classroom', 'Classroom'),
        ('events', 'Events'),
        ('activities', 'Activities'),
        ('others', 'Others'),
    ]

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    show_on_homepage = models.BooleanField(default=False, help_text="Check to show this image on the homepage.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title