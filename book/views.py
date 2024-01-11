from django.shortcuts import render
from .models import Book
# Create your views here.

def home(request):
    return render(request,'index.html')


def aloqa(request):
    return render(request,'contact.html')


def blog(request):
    return render(request,'blog.html')


def list(request):
    books=Book.objects.all()
    context={
        'books':books
    }
    return render(request,'books-media-gird-view-v2.html',context)


def new(request):
    return render(request,'news-events-list-view.html')


def fo(request):
    return render(request,'404.html')


def BlogDetail(request):
    return render(request,'blog-detail.html')


def books_media_detail(request):
    return render(request,'books-media-detail-v1.html')


def books_media2(request):
    return render(request,'books-media-detail-v2.html')


def books_gird(request):
    return render(request,'books-media-gird-view-v1.html')


def cart(request):
    return render(request,'cart.html')


def chekout(request):
    return render(request,'cart.html')


def home2(request):
    return render(request,'home-v2.html')


def news2(request):
    return render(request,'news-events-detail.html')

