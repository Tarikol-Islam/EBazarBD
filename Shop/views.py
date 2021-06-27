from django.shortcuts import render
from django.http import HttpResponse
from Shop.models import product
from math import ceil, prod
# Create your views here.

def index(request):
    products= product.objects.all()
    allProds=[]
    catprods= product.objects.values('product_catg', 'id')
    cats= {item["product_catg"] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(product_catg=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"Shop/index.html", params)

def search(request):
    return render(request,'Shop/search.html')

def productdetails(request, RequiredProductID):
    TheProduct = product.objects.filter(id=RequiredProductID)
    print(TheProduct[0])
    return render(request,'Shop/productdetails.html',{'TheProduct':TheProduct[0]})

def orders(request):
    return render(request,'Shop/orders.html')

def profile(request):
    return render(request,'Shop/profile.html')

def contact(request):
    return render(request,'Shop/contact.html')

def about(request):
    return render(request,'Shop/about.html')