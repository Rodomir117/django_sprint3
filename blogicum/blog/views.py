from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Post, Category


def index(request):
    """Главная страница."""
    template = 'blog/index.html'
    posts_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {'post_list': posts_list[:5]}
    return render(request, template, context)


def post_detail(request, id):
    """Страница отдельной публикации."""
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        id=id,
        is_published=True,
        category__is_published=True,
        pub_date__lt=timezone.now()
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Страница категории."""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category=category
    )
    context = {'category': category,
               'post_list': posts_list}
    return render(request, template, context)
