from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['content', 'image']   # 컬럼중에 어떤 것을 보여줄지 선택하는 항목


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
