# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
''' 
# DONE * Rearrange models' order
# DONE * Make sure each model has one field with primary_key=True
# DONE * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# DONE * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
Feel free to rename the models, but don't rename db_table values or field names.'''

from django.db import models
from django.db.models import Q


class FoodDescription(models.Model):
    fdc_id = models.IntegerField(primary_key=True,unique=True)
    description = models.TextField(blank=True, null=True,  db_index=True)
    food_category_id = models.IntegerField(blank=True, null=True, unique=True)

    class Meta:
        managed = False
        db_table = 'food_description'
        ordering = ['food_category_id']
        indexes = [
            models.Index(fields=['description'],name="desc",condition=Q(food_category_id__exists=True))
        ]

    def __str__(self):
        return f"{self.description}"

class BrandedFoodCategory(models.Model):
    fdc_id = models.OneToOneField(FoodDescription,to_field="fdc_id",db_column="fdc_id", on_delete=models.DO_NOTHING,primary_key=True)
    ingredients = models.TextField(blank=True, null=True)
    serving_size = models.FloatField(blank=True, null=True)
    serving_size_unit = models.TextField(blank=True, null=True)
    branded_food_category = models.TextField(blank=True, null=True, db_index=True)
    household_serving_fulltext = models.TextField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'branded_food_category'
    
    def __str__(self): 
        return f"{self.branded_food_category}"

class FoodNutrient(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    fdc_id = models.ForeignKey(FoodDescription,db_column="fdc_id", on_delete=models.DO_NOTHING, null=True)
    nutrient_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_nutrient'


    def __str__(self):
        return f"FoodNut:{self.amount}"


class FoodCategory(models.Model):
    id = models.OneToOneField(FoodDescription ,to_field="food_category_id",db_column='id' ,primary_key=True,on_delete=models.DO_NOTHING)
    code = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_category'
        ordering = ['description']

    def __str__(self):
        return f"{self.description}"

class FoodPortion(models.Model):
    fdc_id = models.ForeignKey(FoodDescription,db_column="fdc_id" ,on_delete=models.DO_NOTHING,blank=True, null=True)
    id = models.IntegerField(primary_key=True,unique=True)
    amount = models.FloatField(blank=True, null=True)
    measure_unit_id = models.IntegerField(blank=True, null=True)
    portion_description = models.TextField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'food_portion'

    def __str__(self):
        return f"{self.portion_description}"


class MeasuringUnit(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'measuring_unit'

    def __str__(self):
        return f"{self.name}"
class Nutrient(models.Model):
    # Food nutrient are defined in 100g/ 100ml units by default, do the conversions for other units 
    id = models.IntegerField(primary_key=True,unique=True)
    name = models.TextField(blank=True, null=True,db_index=True)
    unit_name = models.TextField(blank=True, null=True,db_index=True)
    nutrient_nbr = models.FloatField(blank=True, null=True,db_index=True)
    rank = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nutrient'

    def __str__(self):
        return f"{self.name},{self.unit_name}"