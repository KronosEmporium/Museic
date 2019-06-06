from django.shortcuts import render, get_object_or_404
from .models import Song, Artist, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'reviews/index.html')

def getsongs(request):
    song_list = Song.objects.all()
    return render(request, 'reviews/songs.html', {'song_list' : song_list})

def getartists (request):
    artist_list = Artist.objects.all()
    return render(request, 'reviews/artists.html', {'artist_list' : artist_list})

def getreviews (request):
    review_list = Review.objects.all()
    return render(request, 'reviews/reviews.html', {'review_list' : review_list})

def songdetails (request, id):
    song = get_object_or_404(Song, pk = id)
    request.GET.get('sort', '-reviewdatetime')
    context = {
        'song' : song,
    }
    return render(request, 'reviews/songdetails.html', context = context)

def reviewdetails (request, id):
    rev = get_object_or_404(Review, pk = id)

    context = {
        'rev' : rev,
    }
    return render(request, 'reviews/reviewdetails.html', context = context)