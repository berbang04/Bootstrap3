from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from .models import Person
from django.template.defaultfilters import slugify


def login_view(request):
    
    if request.user.is_authenticated:
        messages.info(request,f'{request.user.username} login olmuş ztaen.')
        return redirect('home_view')
    context=dict()
    if request.method=="POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        # if len(username) <6 or len(password)<6:
        #     messages.warning(request,'adam gibi şifre gir')
        #     return render(request,'user_profile/login.html',context)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'{request.user.username} login oldunuz ')
            return redirect('home_view')
    return render(request,'user_profile/login.html',context)


def logout_view(request):
    messages.info(request,f'{request.user.username} logout oldun bro')
    logout(request)
    return redirect('home_view')

def register_view(request):
    context=dict()
    if request.method=='POST':
        p=request.POST
        username=p.get('username')
        
        email=p.get('email')
        email_confirm=p.get('email_confirm')
        password_confirm=p.get('password_confirm')
        password=p.get('password')
        instagram=p.get('instagram')
        print('*'*30)
        print(username,email,email_confirm,password,password_confirm,instagram)
        print('*'*30)
        print(request.POST)
        if len(email)<3 or len(password)<3 or len(username)<3 :
            messages.warning(request,"bilgiler en az dört karakterli olur")
            return redirect('user_profile:register_view')

        if email != email_confirm:
            messages.warning(request,"email bilgisini doğru gir")
            return redirect('user_profile:register_view')
        if password != password_confirm:
            messages.warning(request,"şifre bilgisini doğru gir")
            return redirect('user_profile:register_view')
        user, created = User.objects.get_or_create(username=username)
        if not created:
            
            user_login=authenticate(request,username=username,password=password)
            if user is not None:
                messages.info(request,'sen zaten kayıtlısın anasayfaya gidiyon')
                login(request,user_login)
                return redirect('home_view')
            messages.warning(request,f'{username} adresi kayıtlı ama login olamadın logine git')
            return redirect('user_profile:login_view')
        user.email = email
        user.username=username
        user.set_password(password)
        profile, profie_created = Person.objects.get_or_create(user=user)
        profile.instagram=instagram
        profile.slug=slugify(username)
        user.save()
        profile.save()
        messages.success(request, f'{user.username} Sisteme Kaydedildiniz..')
        user_login = authenticate(request, username=username, password=password)
        login(request, user_login)
        return redirect('home_view')

    return render(request,'user_profile/register.html',context)
# Create your views here.
