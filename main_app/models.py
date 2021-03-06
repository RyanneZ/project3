from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here

class Postcreated(models.Model):
  image = models.ImageField(null=False, blank=False)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  tags = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('detail', kwargs={'post_id': self.id})

class Photo(models.Model):
 
  picture = models.FileField(upload_to='media/')
  post = models.ForeignKey(Postcreated(), on_delete=models.CASCADE)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    about = models.CharField(max_length=200)
    image = models.ImageField()
    website = models.URLField(max_length=250)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed



class Comments(models.Model):
  content = models.TextField(max_length=250)
  post = models.ForeignKey(Postcreated, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


class Savedpost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Postcreated,on_delete=models.CASCADE) 
    class Meta:
        unique_together = ["user", "post"]