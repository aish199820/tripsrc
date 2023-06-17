from django.urls import path
from . import views

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('register/',views.register.as_view(),name='register'),
    path('signin/',views.signin.as_view(),name='signin'),
    path('aboutus/',views.aboutus.as_view(),name='aboutus'),
    path('signout/',views.signout.as_view(),name='signout'),
    path('destination/',views.destination.as_view(),name='destination'),
    path('viewdetail/<slug:tour_id>',views.viewdetail.as_view(),name='viewdetail'),
    path('profile/<slug:username>',views.profile.as_view(),name='profile'),
    path('searches/',views.searches.as_view(),name='searches'),
    path('booking/',views.booking.as_view(),name='booking'),
    path('mytrips/',views.mytrips.as_view(),name='mytrips'),
    path('cancelbook/<slug:bookid>',views.cancelbook.as_view(),name='cancelbook'),
    path('state/<slug:destination>',views.state.as_view(),name='state'),
    path('tripstory/',views.tripstory.as_view(),name='tripstory'),
    path('contactus/',views.contactus.as_view(),name='contactus'),
    path('viewbooking/<slug:tour_id>',views.viewbooking.as_view(),name='viewbooking'),


    # admin url
    path('checkbook/',views.checkbook.as_view(),name='checkbook'),
    path('uploadtrip/',views.uploadtrip.as_view(),name='uploadtrip'),
    path('userquery/',views.userquery.as_view(),name='userquery'),
    path('reply/<slug:id>',views.reply.as_view(),name='reply'),
    # path('uploadpackage/',views.uploadpackage.as_view(),name='uploadpackage'),





    

]
