from django.shortcuts import render
from django.http import HttpResponse
from .models import product, contact, yourCart, Order, orderUpdate
from math import ceil
from datetime import date
import json

# Create your views here.

def index(request):
    products = product.objects.all()
    # category = product.objects.values_list('category')     #get all the category in the form of list
    n = len(products)  # lenght of products
    noOfSlides = n//4 + ceil(n/4 - n//4)
    # allProd = [[products,len(products),range(1,noOfSlides)],[products,len(products),range(1,noOfSlides)]]
    # category = ["mens fashion", "womens fashion", "electronics"]

    catElectro = product.objects.filter(category='electronics')
    catMens = product.objects.filter(category='mens fashion')
    catWomens = product.objects.filter(category='womens fashion')
    catPerfume = product.objects.filter(category='perfume')
    n1 = len(catElectro)
    n2 = len(catMens)
    n3 = len(catWomens)
    n4 = len(catPerfume)

    list1 = [(catElectro, range(1, (n1//4 + ceil(n1/4 - n1//4)))), (catMens, range(1, (n2//4 + ceil(n2/4 - n2//4)))),
              (catWomens, range(1, (n3//4 + ceil(n3/4 - n3//4)))), (catPerfume, range(1, (n4//4 + ceil(n4/4 - n4//4))))]
    params = {'products': products, "range": range(
        1, noOfSlides), "length": n, "cats": list1}
    # return HttpResponse("in shop")
    return render(request, "shop/index.html",params)


def about(request):
    return render(request, 'shop/about.html')

 
def tracker(request):
    if request.method == "POST":
        id = request.POST.get('order_Id')
        email = request.POST.get('email')
        print(email)
        try:
            update = Order.objects.filter(order_id=id, email=email)
            str1 = update[0].item_json
            dict1 = json.loads(str1)
            # l1 = str1.split()
            if (len(update) > 0):
                # finding out the your ordered products
                orderedProds = []
                for i in dict1:
                    data5 = product.objects.filter(id=i[4:])
                    orderedProds.append({"product_name": data5[0].product_name, "price": data5[0].price,"quantity":dict1[i]})
                response1 = orderedProds
                # finding out the update status of your respective order id
                updates = []
                data = orderUpdate.objects.filter(order_id=id)
                for item in data:
                    updates.append(
                        {"text": item.update_desc, "time": item.timeStamp})

                response2 = updates
                response = [response1 , response2]
                response = json.dumps(response,default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("{}")
        except Exception as e:
            return HttpResponse("{}")

    return render(request, 'shop/tracker.html')


def contactUs(request):         # change the function name due to we create a model with same name
    if request.method == "POST":
        name = request.POST.get('name', "###")
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('query')
        curr_dat = date.today()
        conatct_data = contact(user=name, phone=phone, email = email, desc = desc, date = curr_dat)
        conatct_data.save()
    return render(request, 'shop/contact.html')


def search(request):
    return render(request, 'shop/search.html')


def checkOut(request):
    lst1 = yourCart.objects.values_list('product_id').last()
    rqrProds = lst1[0]
    data4 = yourCart.objects.filter(product_id=rqrProds)
    str1 = data4[0].items
    l1 = str1.split()               # print(l1)      ['prod13',"1", 'prod14', '2']
    totalCost = 0
    allRqrProdsList = []
    thank = False
    for i in range(0, len(l1), 2):
        data5 = product.objects.filter(id=l1[i][4:])            #l1[i][4:]   ['prod13',"1", 'prod14', '2'] ---> 1
        totalCost += (data5[0].price) * (int(l1[i+1]))          #totalCost = price * int(quantity-->str)
        allRqrProdsList.append(data5)

    if request.method == "POST":
        item_json = request.POST.get('nameJson', " ")
        name = request.POST.get('name', "###")
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('adr1') + " " + request.POST.get('adr2')
        zip = request.POST.get('zip', "###")
        city = request.POST.get('city')
        selectState = request.POST.get('selectState')
        entry = Order(item_json=item_json, name=name, phone = phone, email = email, address = address, zip = zip, city = city, state = selectState)
        entry.save()
        thank = True            
        idObj = Order.objects.last()
        id = idObj.order_id
        ordUpd = orderUpdate(
            order_id=id, update_desc="your order has confirmed for delivery")
        ordUpd.save()

        return render(request, 'shop/checkOut.html', {"thank": thank,"id":id})

    return render(request, 'shop/checkOut.html', {"cartProds": allRqrProdsList,"totalCost":totalCost})

    # print(orderId)
    # return render(request,'shop/checkOut.html',{"cartProds":allRqrProdsList})
    # return render(request,'shop/checkOut.html')

def yourCartItems(request):
    str2 = ""
    if request.method == "POST":
        name = request.POST.get('prodId', "###")
        str2 += name
        data2 = yourCart(items=name)
        data2.save()
    l1 = str2.split()
    # print(l1)      ['prod13',"1", 'prod14', '2']
    allRqrProdsList = []
    for i in range(0, len(l1), 2):

        data3 = product.objects.filter(
            id=l1[i][4:]).values()  # l1[i][4:]) = 13
        # print(data3)
        allRqrProdsList.append(data3)
    # print(allRqrProdsList)

    return render(request, 'shop/yourCart.html', {"cartProds": allRqrProdsList})


def prodView(request, myid):
    prod = product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {"product": prod})
