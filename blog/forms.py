from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Enter Your Name",
            "user_email": "Type in your Email",
            "text": "Your comment about this post"
        }
