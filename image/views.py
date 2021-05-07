from rest_framework import generics

# Create your views here.
from .models import Image
from .serializers import ImageSerializers


class ImageList(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Image.objects.all()
    serializer_class = ImageSerializers


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = Image.objects.all()
    serializer_class = ImageSerializers
