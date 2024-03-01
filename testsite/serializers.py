from .models import Product, Lesson
from rest_framework import serializers


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    included_lessons = LessonSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
