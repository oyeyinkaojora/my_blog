from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.



class Post(models.Model):
    STATUS = (
        (0,"Draft"),
        (1,"Publish")
    )
    author = models.ForeignKey(User,null=True,blank=True, on_delete = models.CASCADE)
    title = models.CharField(max_length=250,blank=True,null=True)
    body = models.TextField(null = True,blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length = 250,null=True)
    status = models.IntegerField(choices=STATUS,default=0)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.pk,self.slug])
        
        





    


    
