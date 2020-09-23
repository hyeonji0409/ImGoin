from django.shortcuts import render, get_object_or_404, redirect
from .models import Market
from django.utils import timezone
from .forms import ProductPost



def home(request):
    return render(request, 'home.html')

def location(request):
    return render(request, 'location.html')

def write(request):
    return render(request, 'write.html')

def account(request):
    return render(request, 'account.html')

def create(request):
   product = Product()
   product.title = request.GET['title']
   product.body = request.GET['body']
   product.pub_date = timezone.datetime.now()
   product.save()
   return redirect('' + str(product.id))

def productpost(request):
    if request.method =='POST':
        form = ProductPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('location')
    else:
        form = ProductPost()
        return render(request,'product.html',{'form':form})

