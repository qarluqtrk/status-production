from django import forms

from app.models import Contact, Comment, Review


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
