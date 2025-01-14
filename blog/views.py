from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post


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
