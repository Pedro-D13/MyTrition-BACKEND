from rest_framework import serializers
from .models import FoodCategory,FoodDescription, FoodNutrient,Nutrient,BrandedFoodCategory

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


class BrandedFoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandedFoodCategory
        fields = ['fdc_id','branded_food_category']

# Helper Function 
def NutritionConverter(self,request,**kwargs):
    nutr = FoodNutrient.objects.filter(fdc_id=self.kwargs['fdc_id_arg'] , nutrient_id__in=self.ids)
    nutr_serializer = FoodNutrientSerializer(nutr, many=True)
    # gets the nutrient info so for protein, carbs, fats, etc 
    result = map(lambda each_nutr: Nutrient.objects.get(id=each_nutr.nutrient_id), nutr)
    serializer = NutrientSerializer(result, many=True)
    zipped_result = zip(serializer.data , nutr_serializer.data)
    final_result = [ dict(**k1, **k2) for (k1,k2) in zipped_result]
    return final_result