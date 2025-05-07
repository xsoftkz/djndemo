from django.shortcuts import render, get_object_or_404
from .models import News

def index(request):
    news_list = News.objects.order_by('-published_at')
    return render(request, 'news/index.html', {'news_list': news_list})

def detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'news/detail.html', {'news': news})

