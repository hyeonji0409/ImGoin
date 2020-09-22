from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone


from .models import Market

def home(request):
    return render(request, 'home.html')

def location(request):
    return render(request, 'location.html')

def write(request):
    return render(request, 'write.html')

def account(request):
    return render(request, 'account.html')

def create(request):
    market = Market()
    market.title = request.GET['title']
    market.place = request.GET['place']
    market.state = request.GET['state']
    market.swap = request.GET['swap']
    market.price = request.GET['price']
    market.content = request.GET['content']
    market.file_route = request.GET['file_route']
    market.tag = request.GET['tag']
    market.save()
    return redirect('/main/' + str(market.id))

