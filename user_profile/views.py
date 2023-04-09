from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
def login_view(request):
    context=dict()
    if request.user.is_authenticated:
        messages.info(request,f'{request.user.username} login olmuş ztaen.')
        return redirect('home_view')
    

    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if len(username) <6 or len(password)<6:
            messages.warning(request,f'adam gibi şifre gir')
            return redirect('login_view')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,f'{request.user.username} login oldunuz ')
            return redirect('home_view')
    return render(request,'user_profile/login.html',context)

def logout_view(request):
    messages.info(request,f'{request.user.username} logout oldun bro')
    logout(request)
    return redirect('home_view')

# Create your views here.
