from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.

class PorfolioViewSet(viewsets.ModelViewSet):
    queryset = Porfolio.objects.all()
    serializer_class = PorfolioSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer