from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    
    
    path('create/', views.create_blog_post_view,name='create_blog_post_view'),
    
]