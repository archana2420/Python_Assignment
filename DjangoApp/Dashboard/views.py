from django.shortcuts import render,redirect
from .models import UserInfo
from .serializers import UserInfoSerializer
from .forms import RegistrationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.
@csrf_exempt
def RegisterationPage(request):
    form=RegistrationForm()
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            serializer=UserInfoSerializer(data=request.POST) # serializes the data
            if serializer.is_valid():
                username = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user=User.objects.filter(username=username)
                if user.exists(): # Checks if the user already exists
                    messages.error(request, 'User already exists!')
                else:
                    user = User.objects.create_user(username=username, password=password) # Creates a user using the credientials
                    user.save()
                    serializer.save()
                    return redirect('dashboard')

            else:
                for i in serializer.errors:
                    if i=='dob':
                        messages.error(request, 'Registration Unsuccessful(Date format:YYYY-MM-DD)')
                    elif i=='name':
                        messages.error(request, 'Registration Unsuccessful!Enter valid name')
                    elif i=='phone_number':
                        messages.error(request, 'Registration Unsuccessful!Enter valid phone number')
                    else:
                        messages.error(request,'Registration Unsuccessful!Enter 8 digit password with alpabets and digits only')


        else:
            messages.error(request, 'Registration Unsuccessful')
    context = {'form': form}
    return render(request, 'Dashboard/Registration.html', context)



def LoginPage(request):
    if request.user.is_authenticated: # To check if the user is already logged in
        return redirect('dashboard')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)
        user=authenticate(request,username=username,password=password) # Verifies the user using password
        if user is not None:
                login(request,user)
                return redirect('dashboard')
        else:
                messages.error(request,'Email/Password is incorrect')

    return render(request,'Dashboard/login.html')

def LogoutPage(request):
    logout(request)
    return render(request, 'Dashboard/logout.html')

@login_required(login_url='login') # Restricts the view to only logged in user
def DashboardPage(request):
    current_user=request.user # Finds the current user
    user_info=UserInfo.objects.get(email=current_user) # Retrieves the current user's information
    context={'name':user_info,'email':user_info.email,'dob':user_info.dob,'phone_number':user_info.phone_number}
    return render(request, 'Dashboard/Dashboard.html',context)