from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def post_list(request):
    return render(request, 'post_list.html', {'post_list':Post.objects.all()})
    #return HttpResponse()
