from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    phone=models.IntegerField(null=True)
    is_vendor=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=True)



#one to one Link
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('created',instance)
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print(instance,"save user profile")
    instance.profile.save()

