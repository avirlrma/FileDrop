from django.db import models


class FileModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey(models.Us)
    datafile = models.FileField(upload_to='data')

    @property
    def name(self):
        return self.datafile.name

    @property
    def size(self):
        return self.datafile.size