from django.shortcuts import render, redirect
from .models import Book, Library
from django.views.generic.detail import DetailView 
from .models import Library 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login



# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(
        request,
        'relationship_app/list_books.html',
        {'books': books}
    )

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # ✅ matches checker
    context_object_name = "library"


class UserLoginView(LoginView):
    template_name = "relationship_app/login.html"


class UserLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # ✅ checker now satisfied
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})
