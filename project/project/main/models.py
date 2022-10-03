from django.db import models


class Plants(models.Model):
    choiceLight = (
        ('Светолюбивое','Светолюбивые'),
        ('Теневыносливое', 'Теневыносливые')
    )
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='static/images/plants/')
    price = models.IntegerField()
    description = models.TextField(null=True) 
    light = models.CharField(choices=choiceLight, max_length=30)
    availability = models.BooleanField()

    def __str__(self):
        return self.title

class ForPlants(models.Model):
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='static/images/forPlants/')
    price = models.IntegerField()
    description = models.TextField(null=True) 
    volume = models.CharField(max_length=250)
    availability = models.BooleanField()

    def __str__(self):
        return self.title

class OceanTheme(models.Model):
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='static/images/oceanTheme/')
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True) 
    availability = models.BooleanField()

    def __str__(self):
        return self.title