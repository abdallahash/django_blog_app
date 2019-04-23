from django.urls import path
from . import views 

urlpatterns = [
    path('', views.post_list, name='post_list'),

    #selfengineered/post/2/
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    #selfengineered/post/new/
    path('post/new', views.post_new, name='post_new'),
]