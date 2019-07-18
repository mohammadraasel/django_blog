from django.shortcuts import render
from .models import Post
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.


def home(request):
    posts = Post.objects.order_by('created_at')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)
    context = {
        "posts": paged_posts
    }
    return render(request, 'blog/home.html', context)


def PostDetail(request, post_id):
    posts = Post.objects.filter(pk=post_id)
    posts ={
        'posts' : posts
    }
    return render(request, 'blog/post/post.html', posts)


def about(request):
    return render(request, 'blog/about.html', {'title': "About"})
