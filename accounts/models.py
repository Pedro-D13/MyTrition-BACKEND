import json
from django.db import models

from django.db.models.signals import post_save, pre_save,Signal

from django.dispatch import receiver

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

from foodsearch.serializers import FoodNutrientSerializer, NutrientSerializer
from foodsearch.models import FoodNutrient, Nutrient

from django.core.signals import request_finished
import logging



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goals = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class FavFoodList(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fdc_id = models.IntegerField(unique=True)
    description = models.TextField(blank=False,null=True)
    nutr_vals = JSONField(blank=True,null=True)
    

    def __str__(self):
        return f"FavFood:{self.description}"

@receiver(pre_save,sender=FavFoodList)        
def NutritionConverter(sender,instance,**kwargs):
    ids=[2000,1003,1004,1008,1005]
    nutr = FoodNutrient.objects.filter(fdc_id=instance.fdc_id,nutrient_id__in=ids) 
    nutr_serializer = FoodNutrientSerializer(nutr,many=True) 
    result = map(lambda each_nutr: Nutrient.objects.get(id=each_nutr.nutrient_id), nutr) 
    serializer = NutrientSerializer(result,many=True) 
    zipped_result = zip(serializer.data,nutr_serializer.data) 
    # lesson learned, do not encode to json more than once otherwise you will get backslashes
    final_result = [dict(**k1,**k2) for (k1,k2) in zipped_result] 
    instance.nutr_vals = final_result
