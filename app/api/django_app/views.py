from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from .models import Author, Quote
from notes import get_notes, get_note, create_note, remove_note, update_note, update_status_note

@login_not_required
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'quotes/author_list.html', {'authors': authors})

@login_not_required
def view_author(request, author_id):
    author = Author.objects.get(id=author_id)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'quotes/view_author.html', {'author': author, 'quotes': quotes})

@login_not_required
def view_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    return render(request, 'quotes/view_quote.html', {'quote': quote})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user  # Пов'язуємо автора з користувачем
            author.save()  # Зберігаємо автора
            return redirect('authors_list')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user  # Пов'язуємо цитату з користувачем
            quote.save()  # Зберігаємо цитату
            return redirect('quote_list')
    else:
        form = QuoteForm()

    return render(request, 'add_quote.html', {'form': form})


@login_not_required
def edit_quote(request, quote_id):
    quote = Quote.objects.get(pk=quote_id)
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect('quote_list')
    else:
        form = QuoteForm(instance=quote)

    return render(request, 'edit_quote.html', {'form': form, 'quote': quote})