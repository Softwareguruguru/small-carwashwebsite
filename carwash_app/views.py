from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import User,Pay,Message
from django.contrib import messages
from django.contrib.auth.models import  auth
import csv

# Create your views here.
def index(request):
    context = {
        'name' : 'B'     
    }
    return render(request,'index.html', context)


def register(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']
        
        if password == password2:  # are the  password the same?
            if User.objects.filter(email=email).exists():  # check if email already exist
                messages.info(request, 'Email Already Exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exist')
                return redirect('register')
            else: # if the above is false
                user =User(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            # check if passwords ot the same
            messages.info(request, 'Password not the same')
            return redirect('register')
        
    else:       
        return render(request,'register.html')
    
    
def login(request):
    if request.method == 'POST':
        usernam = request.POST['username']
        passwor = request.POST['password']
        users = auth.authenticate(username=usernam,password=passwor)
        
        if users is not None:
            auth.login(request,users)
            return redirect('home')
        else:
            messages.info(request,'credentials invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    writer =csv.writer(response)
    writer.writerow(['Username','Email','Password'])
    for admins in User.objects.all().values_list('username','email','password'):
        writer.writerow(admins)
        
    response['Content_Disposition'] ='attachment;filename "users.csv"'
    return response


    
def home(request):
    return render(request,'home.html')

def contacts(request):
      if request.method == 'POST':
            #fetching data  entries from inputs
            numbers  = request.POST['number']
            emails = request.POST['email']
            select_services = request.POST['select_service']
            requirement = request.POST['requirements']
            #saving data to the database
            sms = Message( number= numbers , email= emails, select_service= select_services,requirements=requirement )
            sms.save()
            return HttpResponse('Data saved')
      else:
           return render(request,'contacts.html')
    
    
   

def pay(request):
    if request.method == 'POST':
        #fetching data  entries from inputs
        fname  = request.POST['fullname']
        mpesa = request.POST['mpesacontact']
        amt = request.POST['amount']
        #saving data to the database
        mydb = Pay(fullname=fname, mpesacontact= mpesa, amount= amt)
        mydb.save()
        return HttpResponse('Data saved')
    
    else:
        return render(request, 'pay.html')
    



def payment_csv(request):
    response = HttpResponse(content_type='text/csv')
    writer =csv.writer(response)
    writer.writerow(['fullname','mpesacontact','amount'])
    for pays in Pay.objects.all().values_list('fullname','mpesacontact','amount'):
        writer.writerow(pays)
        
    response['Content_Disposition'] ='attachment;filename "payment.csv"'
    return response   

def events(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = User.objects.filter(username__icontains=q)
    else:
        data = User.objects.all()
    
    
    data = User.objects.all()
    context = {
        'data':data
    }
    return render(request,'events.html',context)
 
