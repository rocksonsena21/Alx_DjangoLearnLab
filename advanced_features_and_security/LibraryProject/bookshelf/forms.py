from django import forms
from .models import Book

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=255)
    author = forms.CharField(max_length=255)
    published_date = forms.DateField(required=False)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

