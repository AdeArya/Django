from django.db import models

from django.utils.text import slugify

class ModelsListView(models.Model):
    nama = models.CharField(max_length = 255)
    quotes = models.CharField(max_length = 255)
    publish = models.DateTimeField(auto_now_add =  True)
    update = models.DateTimeField(auto_now = True)
    slug = models.SlugField(blank = True, editable = False)

    def save(self):
        self.slug = slugify(self.nama)
        super(ModelsListView, self).save()

    def __str__(self):
        return "{}.{}".format(self.id, self.nama)