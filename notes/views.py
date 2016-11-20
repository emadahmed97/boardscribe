from django.shortcuts import render
from django.http import HttpResponse
from .models import Classes,Notes

# Create your views here.
def index(request):
    latest_post_list = Classes.objects.order_by('-title')[:10]
    print latest_post_list
    context = {'latest_post_list':latest_post_list }
    return render(request, 'notes/index.html',context)

def detail(request,article_id):
    latest_post_list = Classes.objects.order_by('-title')[:10]
    article = Notes.objects.get(pk=article_id)
    print latest_post_list
    context = {'latest_post_list':latest_post_list, 'article':article }
    return render(request, 'notes/index.html',context)
