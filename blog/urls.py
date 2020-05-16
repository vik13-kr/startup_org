from django.conf.urls import url
from django.urls import path

from .import views
from .views import PostCreate, PostUpdate

urlpatterns = [
    path('blog/',views.post_list, name = 'blog_post_list'),
    path('blog/<int:year>/<int:month>/<slug:slug>/',views.post_detail, name = 'blog_post_detail'),
    path('blog/create/', PostCreate.as_view(), name = 'blog_post_create'),
    path('<int:year>/<int:month>/<slug:slug>/update', PostUpdate.as_view(), name = 'blog_post_update')

]
   