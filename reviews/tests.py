from django.test import TestCase
from reviews.models import Song, Artist, Review, UserProfile
from reviews.views import index, getsongs, getartists, getreviews, songdetails, reviewdetails
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class SongTest(TestCase):
    def test_string(self):
        song = Song(songtitle = "Hey Jude")
        self.assertEqual(str(song), song.songtitle)
        
    def test_table(self):
        self.assertEqual(str(Song._meta.db_table), "song")

class ArtistTest(TestCase):
    def setup(self):
        artist = Artist(artistname = "The Beatles")
        song = Song(songartist = artist, songtitle = "Hey Jude")
        return song

    def test_song(self):
        song = self.setup()
        self.assertEqual(str(song.songartist), "The Beatles")

    def test_table(self):
        self.assertEqual(str(Artist._meta.db_table), "artist")

class ReviewTest(TestCase):
    def test_string(self):
        rev = Review(reviewtitle = "I like Hey Jude")
        self.assertEqual(str(rev), rev.reviewtitle)

    def test_table(self):
        self.assertEqual(str(Review._meta.db_table), "review")

class IndexTest(TestCase):
    def test_view_url_accessible(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

class GetSongsTest(TestCase):
    def test_view_url_accessible(self):
        response = self.client.get(reverse("songs"))
        self.assertEqual(response.status_code, 200)

    def setup(self):
        artist = Artist.objects.create(artistname = "The Beatles", artistgenre = "Rock", artistrating = 0)
        song = Song.objects.create(songtitle = "Hey Jude", songlink = "www.google.com", songartist = artist, songrating = 0, ratingcount = 0)
        return song
    
    def test_song_detail_success(self):
        deets = self.setup()
        response = self.client.get(reverse("songdetails", args = (deets.id,)))
        self.assertEqual(response.status_code, 200)

class GetArtistsTest(TestCase):
    def test_view_url_accessible(self):
        response = self.client.get(reverse("artists"))
        self.assertEqual(response.status_code, 200)

class GetReviewsTest(TestCase):
    def test_view_url_accessible(self):
        response = self.client.get(reverse("reviews"))
        self.assertEqual(response.status_code, 200)

    def setup(self):
        u = User.objects.create(username = 'myuser')
        artist = Artist.objects.create(artistname = "The Beatles", artistgenre = "Rock", artistrating = 0)
        song = Song.objects.create(songtitle = "Hey Jude", songlink = "www.google.com", songartist = artist, songrating = 0, ratingcount = 0)
        rev = Review.objects.create(reviewtitle = "Hey Jude is pretty good", reviewdatetime = "June 10, 2019, 3:30 a.m.", reviewuser = u, reviewsong = song, reviewtext = "The title says it all.", reviewupvotes = 0, reviewdownvotes = 0, uservote = 0)
        return rev
    
    def test_review_detail_success(self):
        deets = self.setup()
        response = self.client.get(reverse("reviewdetails", args = (deets.id,)))
        self.assertEqual(response.status_code, 200)

class New_Review_authentication_test(TestCase):
    def setUp(self):
        self.test_artist = Artist.objects.create(artistname = "The Beatles", artistgenre = "Rock", artistrating = 0)
        self.test_song = Song.objects.create(songtitle = "Hey Jude", songlink = "www.google.com", songartist = self.test_artist, songrating = 0, ratingcount = 0)
        self.test_user = User.objects.create_user(username = 'testuser1', password = 'P@ssw0rd1')
        self.type = Review.objects.create(reviewtitle = "Hey Jude is pretty good", reviewdatetime = "June 10, 2019, 3:30 a.m.", reviewuser = self.test_user, reviewsong = self.test_song, reviewtext = "The title says it all.", reviewupvotes = 0, reviewdownvotes = 0, uservote = 0)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newreview'))
        self.assertRedirects(response, '/accounts/login/?next=/reviews/newReview/')

    def test_Logged_in_uses_correct_template(self):
        login = self.client.login(username = 'testuser1', password = 'P@ssw0rd1')
        response = self.client.get(reverse('newreview'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/newreview.html')
