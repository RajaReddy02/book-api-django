from rest_framework import viewsets
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]