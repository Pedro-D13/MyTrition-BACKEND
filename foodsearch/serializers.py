from rest_framework import serializers
from .models import FoodCategory,FoodDescription, FoodNutrient,Nutrient

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ['id','description']


class FoodDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDescription
        fields = ['fdc_id','description','food_category_id']

class FoodNutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodNutrient
        fields = ['amount']


class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields= ['name','unit_name']

