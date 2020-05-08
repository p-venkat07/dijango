from django.db import models
# Create your models here.
class Member(models.Model):
    name        = models.CharField(max_length=100)
    img         = models.ImageField(upload_to ='pics' )
    designation = models.TextField()


    def __str__(self):
        return self.name

class year(models.Model):
    year   = models.IntegerField()
    members= models.ManyToManyField(Member)
    
