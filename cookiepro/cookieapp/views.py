from django.shortcuts import render
from django.http import HttpResponse
def create_cookie(request):
    if not request.COOKIES.get('color'):
        response=HttpResponse("cookie is created")
        response.set_cookie('color','blue')
        return response
    else:
        return HttpResponse("your favourite""color is {0}".format(request.COOKIES['color']))
def count_cookie(request):
    if not request.COOKIES.get('visits'):
        response=HttpResponse("this is your first visit to the site.""from now on i will track""your visits to this site.")
        response.set_cookie('visits','1')
    else:
        visits=int(request.COOKIES.get('visits'))+1
        response=HttpResponse("this is your {0} visit".format(visits))
        response.set_cookie('visits',str(visits))
        return response
def delete_cookie(request):
    if request.COOKIES.get('visits'):
        response=HttpResponse("cookies cleared")
        response.delete_cookie("visits")
    else:
        response=HttpResponse("we are not tracking you.")
    return response  
        
    
        
    
    
    
