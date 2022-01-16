from django.shortcuts import render,redirect
from .models import UserInfo
from .serializers import UserInfoSerializer
from .forms import LoginForm,RegistrationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
@csrf_exempt
def RegisterationPage(request):
    form=RegistrationForm()
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user = User.objects.create_user(username=username,password=password)
            user.save()
            serializer=UserInfoSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return redirect('dashboard')
            else:
                print("serializer error",serializer.errors)
        else:
            print(form.errors)

    context={'form':form}
    return render(request,'Dashboard/Registration.html',context)

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    # if request.method=="POST":
    #     email=request.POST['email']
    #     password=request.POST['password']
    #     print(email,password)
    #     user=UserInfo.objects.filter(email=email)
    #     if user is not None:
    #         user=UserInfo.objects.get(email=email)
    #         print(user)
    #         if user.password==password:
    #             return redirect('dashboard',email=user.email)
    #     else:
    #         print('User Not Found')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.get(username=username)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')

    return render(request,'Dashboard/login.html')

def LogoutPage(request):
    logout(request)
    return render(request, 'Dashboard/logout.html')

@login_required(login_url='login')
def DashboardPage(request):
    current_user=request.user
    print(current_user)
    user_info=UserInfo.objects.get(email=current_user)
    print(user_info.dob)
    context={'name':user_info,'email':user_info.email,'dob':user_info.dob,'phone_number':user_info.phone_number}
    return render(request, 'Dashboard/Dashboard.html',context)