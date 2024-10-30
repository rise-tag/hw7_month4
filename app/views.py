from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Article  # Импортируем модель статьи

def blog_list(request, article_id=None):
    if article_id:
        post = get_object_or_404(Article, id=article_id)
        return render(request, 'blog_detail.html', {'post': post})
    else:
        articles = Article.objects.all()
        return render(request, 'blog_list.html', {'articles': articles})
