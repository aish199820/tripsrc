from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from .models import ProfileModel,BookingModel,TripStoryModel,ContactUsModel

class LoginForm(AuthenticationForm):
    
    username= forms.CharField(label='Enter Your Username',widget=forms.TextInput(attrs={'class':'form-control'}))

    password= forms.CharField(label='Enter Your Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class RegisterForm(UserCreationForm):

    password1= forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2= forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

        labels={
            'username':'Enter Username',
            'first_name':'Enter First Name',
            'last_name':'Enter Last Name',
            'email':'Enter Email-Id' 
        }


        widgets={

            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})

        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['username','contact','address','email']

        labels={
            'username':'Enter Username',
            'contact':'Update Contact Number',
            'address':'Update Your Address',
            'email':'Update Email-ID'
        }

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control','placeholder':'add address'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})

        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = ['bookid','tour_id','user_name','contact','from_location','to_location','price','numdays','payment_method','status','people']
    

        labels={
                'bookid':'Enter Username',
                'tour_id':'Update tour id',
                'user_name':'Update user',
                'contact':'Update contact',
                'from_location':'from_location',
                'to_location':'to_location',
                'price':'price',
                'numdays':'numdays',
                'payment_method':'payment_method',
                'status':'status',
                'people':'people'

            }


class tripstoryform(forms.ModelForm):
    class Meta:
        model = TripStoryModel
        fields = ['storytype','username','image','desc']


        labels ={
            'storytype' : 'enter type',
            'username' : 'Enter Your User Name',
            'image' : 'Upload Image',
            'desc' : 'Enter Descriptions',
        }

        widgets = {

            'storytype':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),

        }

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ['name','email','feedback','reply']

        labels = {
            'name': 'Enter Your Name',
            'email': 'Enter Your Email',
            'feedback': 'Enter Your Feedback Or any Query',
            'reply':'Reply'
        }

        widgets = {

            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'feedback':forms.Textarea(attrs={'class':'form-control'}),
            'reply':forms.Textarea(attrs={'class':'form-control'})

        }


# class UploadPackageForm(forms.ModelForm):
#     class Meta:
#         model = PackageModel
#         fields = ['tour_id','destination','state','city','place_info','places','places1','places2','places3','from_date','to_date','day_one','day_two','day_three','day_four','day_five','tour_info','from_location','to_location','price','meet_time','cancel_policy','numdays']

#         labels = {
#             'tour_id': 'Enter Tour_Id',
#             'destination': 'Enter Destination',
#              'state': 'Enter State',
#              'city': 'Enter City',
#              'place_info': 'Enter Place Information',
#              'places': 'Upload image',
#              'places1': 'Upload image',
#              'places2': 'Upload image',
#              'places3': 'Upload image',
#              'from_date': 'Select From Date',
#              'to_date': 'Select To Date',
#              'day_one': 'Enter Day1 Itinary',
#               'day_two': 'Enter Day2 Itinary',
#               'day_three': 'Enter Day3 Itinary',
#               'day_four': 'Enter Day4 Itinary',
#               'day_five': 'Enter Day5 Itinary',
#               'tour_info': 'Enter Tour Information',
#               'from_location': 'Enter From Location',
#               'to_location': 'Enter To Location',
#               'price': 'Enter Price',
#               'meet_time': 'Enter Meet Time',
#               'cancel_policy': 'Enter Cancellation Policy',
#               'numdays': 'Number Of Days'
        # }

        # widgets = {

        #     'tour_id':forms.TextInput(attrs={'class':'form-control'}),
        #     'destination': forms.TextInput(attrs={'class':'form-control'}),
        #     'state': forms.TextInput(attrs={'class':'form-control'}),
        #     'city': forms.TextInput(attrs={'class':'form-control'}),
        #     'place_info': forms.Textarea(attrs={'class':'form-control'}),
        #     'places': forms.FileInput(attrs={'class':'form-control'}),
        #     'places1': forms.FileInput(attrs={'class':'form-control'}),
        #     'places2': forms.FileInput(attrs={'class':'form-control'}),
        #     'places3': forms.FileInput(attrs={'class':'form-control'}),
        #     'from_date': forms.DateInput(attrs={'class':'form-control'}),
        #     'to_date':  forms.DateInput(attrs={'class':'form-control'}),
        #     'day_one': forms.Textarea(attrs={'class':'form-control'}),
        #     'day_two': forms.Textarea(attrs={'class':'form-control'}),
        #     'day_three': forms.Textarea(attrs={'class':'form-control'}),
        #     'day_four': forms.Textarea(attrs={'class':'form-control'}),
        #     'day_five': forms.Textarea(attrs={'class':'form-control'}),
        #     'tour_info': forms.Textarea(attrs={'class':'form-control'}),
        #     'from_location': forms.TextInput(attrs={'class':'form-control'}),
        #     'to_location': forms.TextInput(attrs={'class':'form-control'}),
        #     'price': forms.NumberInput(attrs={'class':'form-control'}),
        #     'meet_time': forms.DateTimeInput(attrs={'class':'form-control'}),
        #     'cancel_policy':forms.TextInput(attrs={'class':'form-control'}),
        #     'numdays': forms.NumberInput(attrs={'class':'form-control'}),


        # }