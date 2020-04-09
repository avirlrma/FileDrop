from django.db import models


class FileModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    datafile = models.FileField()