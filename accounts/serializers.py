from .models import Profile, FavFoodList
from rest_framework import serializers


class FavFoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavFoodList
        fields = ['description', 'fdc_id','nutr_vals']
