from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Song (models.Model):
    songtitle = models.CharField(max_length = 255)
    songlink = models.URLField()
    # songartist = models.ForeignKey
    songrating = models.IntegerField(default = 0)
    ratingcount = models.IntegerField(default = 0)
    songreviews = models.ManyToManyField( 'Review', blank=True )
    # ORDER_CHOICES = [
    #     ("N", "New"),
    #     ("U", "Upvotes"),
    #     ("D", "Downvotes"),
    # ]
    # revieworder = models.CharField(
    #     max_length=1,
    #     choices=ORDER_CHOICES,
    #     default="N",
    # )

    def __str__(self):
        return self.songtitle

    def calcRating(self):
        return float(self.songrating / self.ratingcount)
    
    class Meta():
        db_table = "song"
        verbose_name_plural = "songs"

class Artist (models.Model):
    artistname = models.CharField(max_length = 255)
    artistgenre = models.CharField(max_length = 255)
    artistrating = models.FloatField(default = 0.0, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    artistsongs = models.ManyToManyField( Song, blank = True )

    def __str__(self):
        return self.artistname
    
    class Meta():
        db_table = "artist"
        verbose_name_plural = "artists"

class Review (models.Model):
    reviewtitle = models.CharField(max_length = 255)
    reviewdatetime = models.DateTimeField(auto_now_add = True)
    reviewuser = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    reviewsong = models.ForeignKey(Song, on_delete = models.DO_NOTHING)
    reviewtext = models.TextField(null = True, blank = True)
    reviewupvotes = models.IntegerField(default = 0)
    reviewdownvotes = models.IntegerField(default = 0)

    def __str__(self):
        return self.reviewtitle
    
    class Meta():
        db_table = "review"
        verbose_name_plural = "reviews"