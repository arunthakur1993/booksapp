from django import forms
from django.forms import ModelForm
from books.models import Book,Document


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'overview','publication_date','publisher']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ( 'document', )
