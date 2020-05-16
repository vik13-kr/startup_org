from django.conf.urls import url
from django.urls import path

from .import views
from .views import TagCreate, StartupCreate, NewslinkCreate

urlpatterns = [
    
    path('tag/', views.tag_list, name = 'organiser_tag_list'),
    #path('tag/create',views.create_tag, name = 'organiser_tag_create'),
    path('tag/create',TagCreate.as_view(), name = 'organiser_tag_create'),
    
    path('tag/<slug:slug>/',views.tag_detail, name= 'organiser_tag_detail'),
    
    path('startups/',views.startup_list, name = 'organiser_startup_list'),
    
    path('startups/create',StartupCreate.as_view(), name = 'organiser_startup_create'),
    
    path('startups/<slug:slug>',views.startup_detail, name = 'organiser_startup_detail'),
    
    path('newslink/create/', NewslinkCreate.as_view(), name= 'organiser_newslink_create' ),
]
#tag_list
#startup_list
#startup_detail