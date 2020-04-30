from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField()

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

  
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
      

class FoodFavourites(models.Model):
    fdc_id = models.BigIntegerField()



# Create your models here.
