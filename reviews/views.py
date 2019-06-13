from django.shortcuts import render, get_object_or_404
from .models import Song, Artist, Review, UserProfile
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
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    rev = get_object_or_404(Review, pk = id)

    for x in profile.reviewsvotedon.all():
        if id == x.id:
            rev.uservote = x.uservote
            break

    context = {
        'rev' : rev,
    }
    return render(request, 'reviews/reviewdetails.html', context = context)

def loginmessage (request):
    return render(request, 'reviews/loginmessage.html')

def logoutmessage (request):
    return render(request, 'reviews/logoutmessage.html')

@login_required
def newReview (request):
    form = ReviewForm
    if request.method == 'POST':
        form = ReviewForm(request.POST or None, initial={ 'reviewuser': request.user })
        if form.is_valid():
            post = form.save(commit=False)
            post.reviewuser = request.user
            post.save()
            form = ReviewForm()
    else:
        form = ReviewForm()
    return render(request, 'reviews/newreview.html', {'form': form})

def reviewUpvote (request, id):
    rev = get_object_or_404(Review, pk = id)
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    previousvote = None

    for x in profile.reviewsvotedon.all():
        if x.id == id:
            previousvote = x.uservote
            break

    # too lazy to add an ENUM. 
    # 0 is null, 1 is upvote, 2 is downvote
    if previousvote == 0:
        rev.reviewupvotes += 1
    if previousvote == 1:
        return
    elif previousvote == 2:
        rev.reviewdownvotes -= 1
        rev.reviewupvotes += 1

    rev.save()

    rev.uservote = 1
    if previousvote == 0:
        profile.reviewsvotedon.add(rev)
    else:
        profile.reviewsvotedon.remove(rev)
        profile.reviewsvotedon.add(rev)

    context = {
        'rev' : rev,
    }
    return render(request, 'reviews/reviewdetails.html', context = context)

def reviewDownvote (request, id):
    rev = get_object_or_404(Review, pk = id)
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    previousvote = None

    for x in profile.reviewsvotedon.all():
        if x.id == id:
            previousvote = x.uservote
            break

    # I Should Probably Add this stuff To The Models
    if previousvote == 0:
        rev.reviewdownvotes += 1
    if previousvote == 1:
        rev.reviewupvotes -= 1
        rev.reviewdownvotes += 1
    elif previousvote == 2:
        return

    rev.save()

    rev.uservote = 2
    if previousvote == 0:
        profile.reviewsvotedon.add(rev)
    else:
        profile.reviewsvoteon.remove(rev)
        profile.reviewsvotedon.add(rev)

    context = {
        'rev' : rev,
    }
    return render(request, 'reviews/reviewdetails.html', context = context)