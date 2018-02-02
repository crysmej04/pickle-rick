from django.shortcuts import render, redirect
from django.contrib import messages
from models import User, Item
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from datetime import date, timedelta
import datetime
# Create your views here.
def index(request):
    return render(request, 'users_app/index.html')

def register(request):
    errors = User.objects.validate(request.POST)
    if (len(errors)>0):
        for error in errors:
            messages.error(request, error)     
        return redirect (reverse('index'))
    else:
        if request.POST.get("first_name") and request.POST.get("last_name") and request.POST.get("email") and request.POST.get("password") and request.POST.get("date_hired"):
            current_user = User.objects.get(id=request.session["id"])
            user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"],
            password=request.POST["password"], date_hired=request.POST["date_hired"])
            user.save()
            request.session["id"]=user.id   
        return redirect(reverse('success'))

def success(request):
    user = User.objects.get(id = request.session["id"])
    items = Item.objects.all()
    context = {"items":items, "user":user}
    return render(request, 'users_app/success.html', context)

def login(request):
    if (request.POST.get("email")):
        if (User.objects.filter(email=request.POST["email"], password=request.POST["password"]).exists()):
            request.session["id"] = user.id
            return redirect("/success")
        else:
            errors = User.objects.UserExistsLogin(request.POST["email"], request.POST["password"])
            if (len(errors)>0):
                for error in errors:
                    messages.error(request, error)
            return redirect (reverse("index"))
        
    else:
        return redirect("/") 

def item_info(request, id):
    current_user = User.objects.get(id=request.session["id"])
    data = Item.objects.filter(id=id)
    items = Item.objects.all()
    context={"data":data, "items":items}
    return render(request, 'users_app/item_info.html', context)

def add_item(request):
    errors = Item.objects.validate(request.POST)
    if (len(errors)>0):
        for error in errors:
            messages.error(request, error)  
        return redirect (reverse('new_item'))
    else:
        if request.POST.get("product"):
            current_user = User.objects.get(id=request.session["id"])
            item = Item.objects.create(product=request.POST.get("product"), creator = current_user)
            item.save()
            return redirect (reverse("success"))
    print request.POST
    print date_added
    

def new_item(request):
    return render(request,'users_app/add_item.html')
    

def destroy(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('/success')

def join(request, id):
    errors = Item.objects.validate(request.POST)
    prevItem = Item.objects.get(id=id)
    current_user = User.objects.get(id=request.session["id"])

    previouslyUsed = False
    for item in Item.objects.all():
        if item.creator == current_user and item.product == prevItem.product:
            previouslyUsed = True
    
    if previouslyUsed == True:
            messages.error(request,"You've already added this to your wishlist")
            return redirect('/success') 
    else:
        new_item = Item.objects.create(product=prevItem.product, date_added=prevItem.date_added,
        added_by=prevItem.added_by, creator = current_user)
        new_item.save()
        print request.POST
        return redirect('/success')