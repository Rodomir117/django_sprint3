from django.shortcuts import get_object_or_404, render

from .constants import POSTS_PER_MAIN
from .models import Category, Post


def index(request):
    """Главная страница."""
    template = 'blog/index.html'
    posts_list = Post.post_objects.all()
    context = {'post_list': posts_list[:POSTS_PER_MAIN]}
    return render(request, template, context)


def post_detail(request, id):
    """Страница отдельной публикации."""
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.post_objects,
        id=id
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Страница категории."""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    posts_list = Post.post_objects.all().filter(category=category)
    context = {'category': category,
               'post_list': posts_list}
    return render(request, template, context)
