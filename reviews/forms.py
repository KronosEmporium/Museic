from django import forms
from .models import Song, Artist, Review

class ReviewForm (forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'