from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=50, editable=False, blank=False, null=False)
    password = models.CharField(max_length=16, editable=True)
    
    def __str__(self):
        return "%s %s" % (self.email, self.password)
    
class Monsters(models.Model):
    name = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return "%s" % (self.name)