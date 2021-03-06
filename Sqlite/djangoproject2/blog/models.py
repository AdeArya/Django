from django.db import models
from django.utils.text import slugify

class Artikel(models.Model):
    judul   = models.CharField(max_length=100)
    isi     = models.TextField()
    penulis = models.CharField(max_length=100)
    publish = models.DateTimeField(auto_now_add=True)
    update  = models.DateTimeField(auto_now=True)
    slug    = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super(Artikel, self).save()

    def __str__(self):
        return "{}.{}". format(self.id, self.judul)