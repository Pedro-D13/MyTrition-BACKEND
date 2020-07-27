#Apps
from accounts.models import FavFoodList, Profile 
from accounts.serializers import FavFoodListSerializer
from foodsearch.models import FoodDescription, FoodNutrient, Nutrient
#Django core
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# DRF
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins, status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.template.backends import django
from django.db import IntegrityError
from foodsearch.serializers import FoodNutrientSerializer, NutrientSerializer



class AccountsFavFoodListVS(mixins.CreateModelMixin,
                            mixins.ListModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    model = FavFoodList
    serializer_class = FavFoodListSerializer
    ids = [2000,1003,1004,1008,1005] # nutrient id's for Protein , Carbs, Kcal, Fats and sugars 

    def get_queryset(self):
        user = self.request.user
        return user.profile.favfoodlist_set.all()

    def list(self, request,**kwags):
        queryset = self.get_queryset()
        serializer = FavFoodListSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self,request, **kwargs,):
        queryset = self.get_queryset()
        try:
            delete_me= queryset.filter(fdc_id=self.kwargs['fdc_id_arg'])
            delete_me.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        val=self.kwargs['fdc_id_arg']
        food_item = FoodDescription.objects.get(fdc_id=val).description
        try:
            result = FavFoodList(profile=self.request.user.profile,fdc_id=val,description=food_item)
            result.save()
            queryset = self.get_queryset() 
            serializer = FavFoodListSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(f"{food_item} is already saved on your profile",status=status.HTTP_405_METHOD_NOT_ALLOWED)
        