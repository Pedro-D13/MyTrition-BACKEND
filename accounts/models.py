from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    def __str__(self):
        return f"FF: {self.description}"
