from django.contrib import admin
from .models import PackageModel,DestinationModel,ProfileModel,BookingModel,TripStoryModel,ContactUsModel

# Register your models here.

@admin.register(PackageModel)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['tour_id','destination','state','city','place_info','places','places1','places2','places3','from_date','to_date','day_one','day_two','day_three','day_four','day_five','tour_info','from_location','to_location','price','meet_time','cancel_policy','numdays']
    

@admin.register(DestinationModel)
class DestinationAdmin(admin.ModelAdmin):
    list_display=['destination','dphoto','dinfo']

@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display=['username','contact','address','email']

@admin.register(BookingModel)
class BookingAdmin(admin.ModelAdmin):
    list_display=['bookid','tour_id','user_name','contact','from_location','to_location','price','numdays','payment_method','created_at','status','people']


@admin.register(TripStoryModel)
class TripStoryAdmin(admin.ModelAdmin):
    list_display=['storytype','username','image','desc','created_at']

@admin.register(ContactUsModel)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=['id','name','email','feedback','reply']