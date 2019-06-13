from django.contrib import admin
from .models import Song, Artist, Review, UserProfile

# Register your models here.
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Review)
admin.site.register(UserProfile)