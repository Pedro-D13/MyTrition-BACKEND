# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BrandedFoodCategory(models.Model):
    fdc_id = models.BigIntegerField(blank=True, null=True)
    brand_owner = models.TextField(blank=True, null=True)
    gtin_upc = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    serving_size = models.FloatField(blank=True, null=True)
    serving_size_unit = models.TextField(blank=True, null=True)
    household_serving_fulltext = models.TextField(blank=True, null=True)
    branded_food_category = models.TextField(blank=True, null=True)
    data_source = models.TextField(blank=True, null=True)
    modified_date = models.TextField(blank=True, null=True)
    available_date = models.TextField(blank=True, null=True)
    market_country = models.TextField(blank=True, null=True)
    discontinued_date = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branded_food_category'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FoodCategory(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    code = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_category'


class FoodData(models.Model):
    fdc_id = models.BigIntegerField(blank=True, null=True)
    data_type = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    food_category_id = models.FloatField(blank=True, null=True)
    publication_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_data'


class FoodDescription(models.Model):
    fdc_id = models.BigIntegerField(blank=True, null=True)
    data_type = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    food_category_id = models.FloatField(blank=True, null=True)
    publication_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_description'


class FoodNutrient(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
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


class FoodPortion(models.Model):
    fdc_id = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
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


class MeasuringUnit(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'measuring_unit'


class Nutrient(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    unit_name = models.TextField(blank=True, null=True)
    nutrient_nbr = models.FloatField(blank=True, null=True)
    rank = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nutrient'


class UsersFoodfavourites(models.Model):
    fdc_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'users_foodfavourites'


class UsersProfile(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_profile'
