from django.db import models
from notes import get_notes, get_note, create_note, remove_note, update_note, update_status_note

class Author(models.Model):
    name = models.CharField(max_length=255)

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
  