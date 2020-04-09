from rest_framework import serializers
from dropbox.models import FileModel

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = '__all__'
        