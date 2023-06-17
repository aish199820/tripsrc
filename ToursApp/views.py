from django.views import View
from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,ProfileForm,BookingForm,tripstoryform,ContactUsForm
from .models import PackageModel,DestinationModel,ProfileModel,BookingModel,TripStoryModel , ContactUsModel
from django.contrib.auth.models import User
from django .contrib.auth import authenticate, login, logout
from django.contrib import messages
import random as r
import re



# Create your views here.


class home(View):
    def get(self, request):
        data1 = PackageModel.objects.all()[0:4]

        
        context = {'data1':data1}
        return render(request,'ToursApp/home.html',context)

class register(View):
    def get(self,request):
        forms=RegisterForm()
        context={'forms':forms}
        return render(request,'ToursApp/register.html',context)

    def post(self,request):
        forms=RegisterForm()
        if request.method == 'POST':
            forms=RegisterForm(request.POST)
            if forms.is_valid():
                messages.success(request,'Successfully User Registered')
                forms.save()
                # messages.success(request,'Successfully User Registered')
                return redirect('home')
        
        context={'forms':forms}

        return render(request,'ToursApp/register.html',context)
    
class signin(View):
    def get(self,request):
        
        forms=LoginForm()
        context={'forms':forms}
        return render(request,'ToursApp/signin.html',context)

    def post(self,request):
        if request.method == 'POST':

            username= request.POST['username']
            pass1= request.POST['password']

            user= authenticate(username=username, password=pass1)

            if user is not None:

                if username == 'admin':

                    login(request,user)
                    messages.success(request,f'Successfully User {username} Logged in..')
                    return redirect('home')

                else:

                    login(request,user)
                    messages.success(request,f'Successfully User {username} Logged in..')
                    return redirect('home')

            else:

                messages.warning(request,'😔 Something Went Wrong..!!')
                forms=LoginForm()
                context={'forms':forms}
                return render(request,'ToursApp/signin.html',context)


        messages.warning(request,'😔 Something Went Wrong..!!')
        return render(request,'ToursApp/signin.html',context)

class destination(View):
    def get(self,request):
        data= DestinationModel.objects.all()
        print(data)
        data1 = PackageModel.objects.all()
        context = {'data1':data1,'data':data}
       
        return render(request,'ToursApp/destination.html',context)


class state(View):
    def get(self,request,destination):
        data = DestinationModel.objects.all()
        cat=DestinationModel.objects.get(destination=destination)
        data1 = PackageModel.objects.filter(destination=cat)

        context = {'data':data,'data1':data1}

        return render(request,'ToursApp/destination.html',context)





class viewdetail(View):
    def get(self,request,tour_id):

        if request.user.is_authenticated:
            try:

                data = PackageModel.objects.get(tour_id=tour_id)
                userdata = ProfileModel.objects.get(username=request.user)
                a=str(request.user)
                if userdata.username == a:
                    book_id = r.randint(10000000,99999999)
                    # form = BookingForm()
                    context = {'data':data,'book_id':book_id,'userdata':userdata} 
                    return render(request,'ToursApp/viewdetail.html',context)
                    
                else:
                    return redirect('home')


            except:
                messages.warning(request,'update profile')
                return render(request,'ToursApp/profile.html',{'username':request.user})
                
                
        else:
            messages.warning(request,'login now')
            return redirect('destination')


    def post(self,request,tour_id):
        if request.method == 'POST':
            price=request.POST['price']
            people=request.POST['people']
            user_name=request.POST['user_name']
            tour_id=request.POST['tour_id']
            book=request.POST['bookid']

            data=ProfileModel.objects.get(username=user_name)
            data1=PackageModel.objects.get(tour_id=tour_id)
            form=BookingForm()
            
            price=int(price)
            people=int(people)

            Total_amount=price*people

            context={'Total_amount':Total_amount,'data':data,'data1':data1,'book':book,'people':people ,'form':form}
            return render(request,'ToursApp/booking.html',context)



class booking(View):

    def get(self,request):
        return redirect('home')

    def post(self,request):
        print('enter')
        forms = BookingForm()
        book_id=request.POST['bookid']
        tour_id = request.POST['tour_id']
        if request.method == 'POST':
            print('post')
            forms = BookingForm(request.POST)
            if forms.is_valid():
                print('valid')
                messages.success(request, 'Booking successfully done.. is your booking id')
                forms.save()
                return redirect('home')

            else:
                print('invalid')
                messages.warning(request,'Something went wrong')
                return redirect('viewdetail',tour_id=tour_id)
        else:
            print('in')
            messages.warning(request,'Something went wrong')
            return redirect('viewdetail',tour_id=tour_id)
    



class mytrips(View):
    def get(self,request):
        data = BookingModel.objects.filter(user_name=request.user).values()
        e =[]

        for d in data:
            d=d.values()
            for c in d:
                e.append(c)

        try:
            data1 = e[2]

        except:

            data1 = str(e)

        userlogin = str(request.user)

        context={'data':data,'data1':data1,'userlogin':userlogin}
        return render(request,'ToursApp/mytrips.html',context)


class tripstory(View):
    def get(self,request):
        data = TripStoryModel.objects.filter(storytype = 'adminstory')
        data1 = TripStoryModel.objects.filter(storytype = 'userstory')
        userlogin = request.user
        
        form = tripstoryform()
        context = {'data':data,'data1':data1,'form':form,'userlogin':userlogin}
        return render(request,'ToursApp/tripstory.html',context)

    def post(self,request):

        form = tripstoryform()
        if request.method == 'POST':
            form = tripstoryform(request.POST,request.FILES)
            if form.is_valid():
                messages.success(request,'Story added')
                form.save()
                return redirect('tripstory')


            else:
                messages.success(request,'something went wrong')
                return redirect('home')







class cancelbook(View):
    def post(self,request,bookid):
        data=BookingModel.objects.get(bookid=bookid)
        data.delete()
        messages.success(request,'Booking Cancelled successfully')

        return redirect('mytrips')


class viewbooking(View):
    def get(self,request,tour_id):
        data = PackageModel.objects.filter(tour_id=tour_id)
        context = {'data':data}
        return render(request,'ToursApp/viewbooking.html',context)




def contactvalidate(contact):
        p=r'[6-9][0-9]{9}$'

        if re.match(p,contact):
            return True

        else:
            return False


class profile(View):
    def get(self,request,username):
        print(username)
        data = ProfileModel.objects.filter(username=request.user).values()
      
        e = []
        for d in data:
            c = d.values()

            for i in c:
                e.append(i)
        
        try:

            data1 = e[0]

        except:

            data1 = str(e)

        if data1 == username:
            forms = ProfileForm()
            # context={'forms':forms,'user':request.user,'data':data}
            context={'data':data}
            messages.success(request,'Profile Updated')
            # return render(request,'ToursApp/profile.html',context)
            return redirect('home')
            

        else:
            forms = ProfileForm()
            context={'forms':forms,'user':request.user}

            return render(request,'ToursApp/profile.html',context)


    def post(self,request,username):

        forms = ProfileForm()
        if request.method == 'POST':
            userlogin = request.user
            
            contact= request.POST['contact']
            d=contactvalidate(contact)
            print(d)

            if d == True:

                forms=ProfileForm(request.POST)
                if forms.is_valid():
                    messages.success(request,'Profile Updated Successfully')
                    forms.save()
                    return redirect('home')

                else:

                    context={'forms':forms,'user':request.user}
                    return render(request,'ToursApp/profile.html',context)
            else:
                messages.warning(request,'invalid number')
                return redirect('profile',username=userlogin)
        else:
            
            messages.success(request,'Profile Updated Successfully')           
            context={'forms':forms,'user':request.user}
            return render(request,'ToursApp/profile.html',context)

        


class searches(View):
    def get(self,request):
        search = request.GET['search']
        data = PackageModel.objects.filter(state__icontains=search)
        context = {'data':data}
        return render(request,'ToursApp/searches.html',context)
       



class aboutus(View):
    def get(self,request):
        data= DestinationModel.objects.all()
        context = {'data':data}


        return render(request,'ToursApp/about.html',context)



class contactus(View):
    def get(self,request):

        form = ContactUsForm()
        context = {'form':form}

        return render(request,'ToursApp/contactus.html',context)

    def post(self,request):

        form = ContactUsForm()
        if request.method == 'POST':
            form = ContactUsForm(request.POST)
            if form.is_valid():
                messages.success(request,'Request Sent Successfully')
                form.save()
                return redirect('home')

        
            else:
                print('invalid')
                messages.warning(request,'Something Went Wrong')
                return redirect('contactus')

        else:
            print('not post')
            messages.warning(request,'Something Went Wrong')
            return redirect('contactus')






class signout(View):
    def get(self,request):
        logout(request)
        messages.success(request,'Successfully user Logged Out')
        return redirect('home')




# admin section

class checkbook(View):
    def get(self,request):
        data = BookingModel.objects.all()
        context = {'data':data}

        return render(request,'ToursApp/checkbook.html',context)
        


class uploadtrip(View):
    def get(self,request):
        form = tripstoryform()

        context = {'form':form}
        return render(request,'ToursApp/uploadtrip.html',context)

    def post(self,request):
        form = tripstoryform()
        if request.method == 'POST':
            form = tripstoryform(request.POST,request.FILES)
            if form.is_valid():
                messages.success(request,'Successfully Uploaded')
                form.save()
                return redirect('home')


            else:
                messages.warning(request,'Something Went wrong')
                return redirect('uploadtrip')

# class uploadpackage(View):
#     def get(self,request):
#         form = UploadPackageForm()

#         context = {'form':form}
#         return render(request,'ToursApp/uploadpackage.html',context)

#     def post(self,request):
#         form = UploadPackageForm()
#         if request.method == 'POST':
#             form = UploadPackageForm(request.POST,request.FILES)
#             if form.is_valid():
#                 messages.success(request,'Successfully Uploaded')
#                 form.save()
#                 return redirect('home')


#             else:
#                 messages.warning(request,'Something Went wrong')
#                 return redirect('uploadpackage')
    


class userquery(View):
    def get(self,request):

        data = ContactUsModel.objects.filter(reply='')
        form = ContactUsForm()
        context={'data':data,'form':form} 
        return render(request,'ToursApp/userquery.html',context)


class reply(View):
    def post(self,request,id):
        # reply=request.POST['reply']
        data = ContactUsModel.objects.get(id=id)
        data.reply=request.POST['reply']
        data.save()
        messages.success(request,'Successfully replied')
        return redirect('home')