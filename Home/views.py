from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request ,'index.html')
    #  return HttpResponse("This is Home page")
def contact(request):
    return render(request ,'contact.html')
def about(request):
    return render(request ,'about.html')
    
def shoes(request):
    return render(request ,"crousel.html")
def product(request):
    return render(request ,"product.html")
def sports(request):
    return render(request ,"sports.html")
def sneakers(request):
    return render(request ,"sneaker.html")
def checkout(request):
    return render(request ,"checkout.html")