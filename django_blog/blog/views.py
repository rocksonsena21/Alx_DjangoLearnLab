from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import RegisterForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


# ================= HOME & POSTS =================

def home(request):
    return render(request, 'blog/base.html')


def posts(request):
    posts = Post.objects.all().order_by("-published_date")
    return render(request, "blog/posts.html", {"posts": posts})


# ================= AUTH =================

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    else:
        form = RegisterForm()

    return render(request, "blog/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "blog/profile.html")


# ================= POST DETAIL =================

def post_detail(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    comments = post.comments.all().order_by("-created_at")

    form = CommentForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form
    })


# ================= COMMENT CRUD (CLASS-BASED) =================


# CREATE COMMENT
class CommentCreateView(LoginRequiredMixin, CreateView):

    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):

        post = get_object_or_404(Post, id=self.kwargs["pk"])

        form.instance.post = post
        form.instance.author = self.request.user

        return super().form_valid(form)

    def get_success_url(self):

        return reverse_lazy("post_detail", kwargs={
            "post_id": self.object.post.id
        })


# UPDATE COMMENT
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def test_func(self):

        comment = self.get_object()

        return self.request.user == comment.author

    def get_success_url(self):

        return reverse_lazy("post_detail", kwargs={
            "post_id": self.object.post.id
        })


# DELETE COMMENT
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):

        comment = self.get_object()

        return self.request.user == comment.author

    def get_success_url(self):

        return reverse_lazy("post_detail", kwargs={
            "post_id": self.object.post.id
        })
