from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image
from main.models import GameNews
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=None)
    image = models.ImageField(default='profile_pics/default/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user}'


    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Comment(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    news = models.ForeignKey(GameNews, on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', null=True, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.user)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('game_details', args=[self.id])


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
