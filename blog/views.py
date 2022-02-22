from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .forms import CommentCreateForm
from django import forms


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def goodfunc(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.good += 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})


class CommentView(CreateView):
    template_name = 'comment_form.html'
    model = Comment
    form_class = CommentCreateForm

#フォームに入力された情報が正しい場合の処理
    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect('blog/post_detail.html', {'post': post})

#htmlテンプレートに渡すデータを定義
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context