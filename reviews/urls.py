from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getsongs/', views.getsongs, name='songs'),
    path('getartists/', views.getartists, name='artists'),
    path('getreviews/', views.getreviews, name='reviews'),
    path('songdetails/<int:id>', views.songdetails, name='songdetails'),
    path('reviewdetails/<int:id>', views.reviewdetails, name='reviewdetails'),
    path('newReview/', views.newReview, name='newreview'),
    path('reviewUpvote/<int:id>', views.reviewUpvote, name='reviewUpvote'),
    path('reviewDownvote/<int:id>', views.reviewDownvote, name='reviewDownvote'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]