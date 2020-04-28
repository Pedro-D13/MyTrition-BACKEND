# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
''' 
# DONE * Rearrange models' order
# DONE * Make sure each model has one field with primary_key=True
# DONE * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# DONE * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
Feel free to rename the models, but don't rename db_table values or field names.'''

from django.db import models

from django.db import models

class BrandedFoodCategory(models.Model):
    fdc_id = models.BigIntegerField(primary_key=True, unique=True)
    ingredients = models.TextField(blank=True, null=True)
    serving_size = models.FloatField(blank=True, null=True)
    serving_size_unit = models.TextField(blank=True, null=True)
    branded_food_category = models.TextField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'branded_food_category'
    
    def __str__(self):
        return f"{self.branded_food_category}"

class FoodDescription(models.Model):
    fdc_id = models.BigIntegerField(primary_key=True,unique=True)
    data_type = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    food_category_id = models.FloatField(blank=True, null=True)
    publication_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_description'
        ordering = ['food_category_id']

    def __str__(self):
        return f"{self.description}"

class FoodNutrient(models.Model):
    id = models.BigIntegerField(primary_key=True,unique=True)
    fdc_id = models.BigIntegerField(blank=True, null=True)
    nutrient_id = models.BigIntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    data_points = models.FloatField(blank=True, null=True)
    derivation_id = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    median = models.FloatField(blank=True, null=True)
    footnote = models.TextField(blank=True, null=True)
    min_year_acquired = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_nutrient'

    def __str__(self):
        return f"FoodNut:{self.amount}"


class FoodCategory(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    code = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_category'
        ordering = ['description']

    def __str__(self):
        return f"{self.description}"

class FoodPortion(models.Model):
    fdc_id = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True,unique=True)
    seq_num = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    measure_unit_id = models.BigIntegerField(blank=True, null=True)
    portion_description = models.TextField(blank=True, null=True)
    modifier = models.TextField(blank=True, null=True)
    gram_weight = models.FloatField(blank=True, null=True)
    data_points = models.FloatField(blank=True, null=True)
    footnote = models.FloatField(blank=True, null=True)
    min_year_acquired = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_portion'

    def __str__(self):
        return f"{self.portion_description},{self.amount}"


class MeasuringUnit(models.Model):
    id = models.BigIntegerField(primary_key=True,unique=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'measuring_unit'

    def __str__(self):
        return f"{self.name}"


class Nutrient(models.Model):
    # Food nutrient are defined in 100g/ 100ml units by default, do the conversions for other units 
    id = models.BigIntegerField(primary_key=True,unique=True)
    name = models.TextField(blank=True, null=True)
    unit_name = models.TextField(blank=True, null=True)
    nutrient_nbr = models.FloatField(blank=True, null=True)
    rank = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nutrient'

    def __str__(self):
        return f"{self.name},{self.unit_name}"
