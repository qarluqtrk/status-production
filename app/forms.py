from django import forms

from app.models.blog import Comment
from app.models.other import Contact, Review, Booking


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "message")


class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("name", "country", "message")


class BookingModelForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("name", "country", "phone_number")
