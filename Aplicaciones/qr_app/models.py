# qr_app/models.py

from django.db import models
from django.urls import reverse

class WebPage(models.Model):
    url = models.URLField(unique=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('web_page_detail', args=[str(self.id)])
