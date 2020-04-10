from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from dropbox.serializers import FileUploadSerializer
from dropbox.models import FileModel



class FileUploadView(generics.CreateAPIView):
    parser_class = (FileUploadParser,)
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
      file_serializer = FileUploadSerializer(data=request.FILES)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        return Response(status=status.HTTP_200_OK)


class FileView(APIView):

    def get_all(self, request):
        file_list = FileModel.objects.all()
        serializer = FileUploadSerializer(file_list,many=True)
        return Response(serializer.data)

    def get(self, request, pk):
        if pk=='all':
            return self.get_all(request)
        try:
            file_obj = FileModel.objects.get(id=pk)
            ser = FileUploadSerializer(file_obj)
            return Response(ser.data)
        except FileModel.DoesNotExist:
            return Response(status=404)


          