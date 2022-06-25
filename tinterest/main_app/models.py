from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Postcreated(models.Model):
  image = models.CharField(max_length=200)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  tags = models.CharField(max_length=100)

  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def get_absolute_url(self):
    return reverse('detail', kwargs={'post_id': self.id})

class Photo(models.Model):
  url = models.CharField(max_length=200)
  post = models.ForeignKey(Postcreated(), on_delete=models.CASCADE)

  def __str__(self):
      return f"Photo for post_id: {self.post_id} @{self.url}"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
 
    description = models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed
    