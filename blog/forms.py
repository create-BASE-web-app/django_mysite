from django import forms
from .models import Comment

#コメント投稿フォーム
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('target', 'created_at')
