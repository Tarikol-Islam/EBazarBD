from django.shortcuts import render
from django.http import HttpResponse, response
from Shop.models import product,Orders,OrderUpdate
from math import ceil, prod
import json
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
    return render(request,'Shop/productdetails.html',{'TheProduct':TheProduct[0]})
def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip', '')
        phone=request.POST.get('phone', '')
        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id = order.order_id, update_desc = "The Order Has Placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request, 'Shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'Shop/checkout.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('else')
        except Exception as e:
            return HttpResponse(e)

    return render(request, 'shop/tracker.html')

def profile(request):
    return render(request,'Shop/profile.html')

def contact(request):
    return render(request,'Shop/contact.html')

def about(request):
    return render(request,'Shop/about.html')