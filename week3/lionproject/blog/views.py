from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import BlogPost
from django.core.paginator import Paginator


def home(request):
    posts = Post.objects
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    blog_posts = paginator.get_page(page)

    return render(request, 'blog/home.html', {'posts':posts, 'blog_posts':blog_posts})

def detail(request, id):
    post = get_object_or_404(Post, pk = id) #해당 아이디값이 있는 블로그의 오브젝트를 가져오거나 없으면 404에러
    return render(request, 'blog/detail.html', {'post':post})

def blogpost(request):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog:home')
    else:
        form = BlogPost()
        return render(request, 'blog/new.html', {'form':form})

def editpost(request, id):
    update_post = Post.objects.get(id = id)
    if request.method == 'POST':
        form = BlogPost(request.POST, instance=update_post)
        if form.is_valid():
            update_post = form.save(commit=False)
            update_post.pub_date = timezone.now()
            update_post.save()
            return redirect('blog:detail', update_post.id)
    else:
        form = BlogPost(instance=update_post)
        return render(request, 'blog/edit.html', {'form':form})

def delete(request, id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('blog:home')

# def edit(request, id):
#     edit_post = Post.objects.get(id = id) 
#     return render(request, 'blog/edit.html', {'post':edit_post})

# def update(request, id):
#     update_post = Post.objects.get(id = id)
#     update_post.title = request.POST['title']
#     update_post.body = request.POST['body']
#     update_post.pub_date = timezone.now()
#     update_post.save()
#     return redirect('blog:detail', update_post.id)
