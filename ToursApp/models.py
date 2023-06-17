from django.db import models

# Create your models here.

class DestinationModel(models.Model):
    destination = models.CharField(max_length=100,primary_key=True)
    dphoto = models.ImageField(blank=True,upload_to='dphotos/')
    dinfo = models.TextField(blank=True,default=0)
    
    def __str__(self):
        return self.destination

class PackageModel(models.Model):
    tour_id = models.CharField(primary_key=True,max_length=100)
    destination = models.ForeignKey(DestinationModel,on_delete=models.CASCADE)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    place_info = models.TextField(blank=True)
    places = models.ImageField(upload_to='places/' , blank=True)
    places1 = models.ImageField(upload_to='places/' , blank=True)
    places2 = models.ImageField(upload_to='places/' , blank=True)
    places3 = models.ImageField(upload_to='places/' , blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    day_one = models.TextField(blank=True)
    day_two = models.TextField(blank=True)
    day_three = models.TextField(blank=True)
    day_four = models.TextField(blank=True)
    day_five = models.TextField(blank=True)
    tour_info = models.TextField(blank=True)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    price = models.IntegerField()
    meet_time = models.DateTimeField()
    cancel_policy = models.CharField(max_length=100)
    numdays = models.IntegerField(blank=True,default=0)



class ProfileModel(models.Model):
    username = models.CharField(primary_key=True,max_length=100)
    contact = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.username
        

class BookingModel(models.Model):
    bookid = models.CharField(primary_key=True,max_length=100)
    tour_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    price = models.IntegerField()
    numdays = models.IntegerField()
    payment_method = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=100,default='Active')
    people = models.IntegerField(blank=True)


class TripStoryModel(models.Model):
    storytype = models.CharField(max_length=100,default='userstory')
    username =models.CharField(max_length=100)
    image = models.ImageField(upload_to='stories/', blank=True)
    desc = models.TextField(blank=True)
    created_at = models.DateField(auto_now=True)


class ContactUsModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
    reply= models.TextField(blank=True)
    