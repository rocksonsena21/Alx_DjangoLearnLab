from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import RegisterForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'blog/base.html')



def posts(request):

    posts = Post.objects.all().order_by("-published_date")

    return render(request, "blog/posts.html", {"posts": posts})




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


def post_detail(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    comments = post.comments.all().order_by("-created_at")

    if request.method == "POST":

        if not request.user.is_authenticated:
            return redirect("login")

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            return redirect("post_detail", post_id=post.id)

    else:
        form = CommentForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form
    })




@login_required
def edit_comment(request, comment_id):

    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user:
        return redirect("home")

    if request.method == "POST":

        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            return redirect("post_detail", post_id=comment.post.id)

    else:
        form = CommentForm(instance=comment)

    return render(request, "blog/edit_comment.html", {"form": form})




@login_required
def delete_comment(request, comment_id):

    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user:
        return redirect("home")

    post_id = comment.post.id
    comment.delete()

    return redirect("post_detail", post_id=post_id)
