from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250)
    background_image = models.ImageField(upload_to="baner")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title   


class Services(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    description=models.TextField()
    background_image = models.ImageField(upload_to="baner")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title  
    
    def get_images(self):
        return ServiceDescription.objects.filter(services=self)

class ServiceDescription(models.Model):
    services=models.ForeignKey(Services,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="baner/", blank=True, null=True)
    service_description = HTMLField(blank=True, null=True)



class ClientLogos(models.Model):
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.logo.name
    

class Blog(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    date = models.DateTimeField(default=timezone.now)
    description=models.TextField()
    thumbnail_img = models.ImageField(upload_to="blog/")
    img = models.ImageField(upload_to="blog/")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title  
    
    def get_images(self):
        return BlogDescription.objects.filter(blog=self)

class BlogDescription(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="baner/", blank=True, null=True)
    service_description = HTMLField(blank=True, null=True)


class Testimonial(models.Model):
    name = models.CharField(max_length=250)
    description=models.TextField()
    profile_image = models.ImageField(upload_to="testimonial/")
    position = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name   