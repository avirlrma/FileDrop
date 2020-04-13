from rest_framework import serializers
from dropbox.models import FileModel
from django.contrib.auth.models import User

class FileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = FileModel
        fields = ['datafile','size','created','name','owner']
        

class UserSerializer(serializers.ModelSerializer):
    files = serializers.SlugRelatedField(many=True, slug_field='name',queryset=FileModel.objects.all())

    class Meta:
        model = User
        fields = ['username', 'files']

    
