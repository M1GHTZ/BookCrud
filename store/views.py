from django.shortcuts import render
from django.views.generic import View
from store import forms


# Create your views here.
class BookCreateView(View):
    def get(self, request, *args, **kwargs):
        form_instance=forms.BookForm()
        return render(request,"book_add.html",{"form":form_instance} )