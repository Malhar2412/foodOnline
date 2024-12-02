from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile



@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
        print('Profile created')
        if created:
            UserProfile.objects.create(user=instance)
        else: 
            try:
                profile = UserProfile.objects.get(user=instance)
                profile.save()
            except:
                UserProfile.objects.create(user=instance)
                
            
@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, *args, **kwargs):
        print(instance.username,'this user is being saved')
    