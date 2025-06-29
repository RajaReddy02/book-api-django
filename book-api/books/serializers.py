from rest_framework import serializers
from .models import Book, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    added_by = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = '__all__'