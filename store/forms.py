from django import forms

class BookForm(forms.Form):
    title=forms.CharField()
    author=forms.CharField()
    price=forms.IntegerField()
    genre=forms.CharField()
    language=forms.CharField()
    year=forms.CharField()