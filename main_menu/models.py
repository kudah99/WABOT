from django.db import models

class MainMenu(models.Model):
    feature_en = models.CharField(max_length=300)
    feature_sh = models.CharField(max_length=300)
    feature_nd = models.CharField(max_length=300)
    slug = models.SlugField(max_length=30)
    last_updated = models.DateTimeField(auto_now_add=True)
