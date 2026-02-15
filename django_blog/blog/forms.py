from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comment, Post
from taggit.forms import TagWidget  # Import TagWidget for tag input in forms


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

    # Simple validation (recommended)
    def clean_content(self):

        content = self.cleaned_data.get("content")

        if len(content.strip()) < 2:
            raise forms.ValidationError("Comment is too short.")

        return content



class PostForm(forms.ModelForm):

    class Meta:

        model = Post

        fields = ['title', 'content', 'tags']

        widgets = {
            'tags': TagWidget()
     }