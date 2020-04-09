from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.views import APIView
from dropbox.serializers import FileUploadSerializer

from rest_framework.response import Response
from rest_framework import status


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
      print(request.data)    
      file_serializer = FileUploadSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



          