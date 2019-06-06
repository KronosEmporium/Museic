from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getsongs/', views.getsongs, name='songs'),
    path('getartists/', views.getartists, name='artists'),
    path('getreviews/', views.getreviews, name='reviews'),
    path('songdetails/<int:id>', views.songdetails, name='songdetails'),
    path('reviewdetails/<int:id>', views.reviewdetails, name='reviewdetails'),
]