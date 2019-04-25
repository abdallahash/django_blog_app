from django.urls import path
from . import views 

urlpatterns = [
    path('', views.post_list, name='post_list'),

    #selfengineered/post/2/
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    #selfengineered/post/new/
    path('post/new', views.post_new, name='post_new'),

    #selfengineered/post/2/edit/
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    #selfengineered/drafts
    path('drafts/', views.post_draft_list, name='post_draft_list'),

    path('post/<int:pk>/publish/', views.post_publish, name='post_publish')
]