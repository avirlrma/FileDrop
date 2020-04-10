from rest_framework import serializers
from dropbox.models import FileModel

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = ['datafile','size','created','name']


    
