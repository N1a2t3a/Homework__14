from django import forms
from .models import Author, Quote
from notes import get_notes, get_note, create_note, remove_note, update_note, update_status_note

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'
        