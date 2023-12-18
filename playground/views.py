from django.shortcuts import render
from django.http import HttpResponse

# always put request in ()
def say_hello(request):
    #return HttpResponse('Hello Django')
    return render(request, 'hello.html', {'name': 'Danko'})
