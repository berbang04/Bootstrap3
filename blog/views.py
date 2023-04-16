from django.shortcuts import render
from .forms import PostModelForm
from .models import Category,Tag,BlogPost
from django.contrib.auth.decorators import login_required

@login_required(login_url="user:login_view")
def create_blog_post_view(request):
    form=PostModelForm()
    if request.method=="POST":
        form=PostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f=form.save(commit=False)
            f.user=request.user
            f.save()
    context=dict(
        form=form
    )
    return render(request,'blog/blog_view.html',context)