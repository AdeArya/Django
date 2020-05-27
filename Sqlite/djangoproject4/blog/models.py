from django.db import models

class Artikel(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    penulis = models.CharField(max_length=100)

    def __str__(self):
        return "{}.{}".format(self.id, self.judul)