from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Cart, CartItem
from tags.models import TaggedItem

# always put 'request' in ()
def say_hello(request):
    # Every class has the 'objects' atribute that returns a manager which is an interface of the db
    # querry_set is lazy
    # __ for relationship when using an object method 
    # __range -> lookup type
    
    return render(request, 'hello.html', {'name': 'Dan'})
