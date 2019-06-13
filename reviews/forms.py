from django import forms
from .models import Song, Artist, Review, UserProfile

class ReviewForm (forms.ModelForm):
    class Meta:
        model = Review
        fields = ('reviewtitle','reviewsong','reviewtext')
        labels = {
            'reviewtitle' : 'Review Title',
            'reviewsong' : 'Song',
            'reviewtext' : '',
        }