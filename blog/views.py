from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone 
from .models import Post 
from .forms import PostForm, CommentForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_list.html', stuff_for_frontend)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blog/post_detail.html', stuff_for_frontend)

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        #to make sure the user in entering a valid stuff and not trying to hack us.
        if form.is_valid():
            #False commit means saving without adding the stuff to the database.
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post= form.save(commit=False)   
            post.author = request.user 
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form, 'post': post}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)

@login_required
def post_draft_list(request):
    draft_posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    stuff_for_frontend = {'draft_posts': draft_posts}
    return render(request, 'blog/post_draft_list.html', stuff_for_frontend)

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)    
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_to_post.html', {'form': form})