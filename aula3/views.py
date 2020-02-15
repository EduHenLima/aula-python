from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.utils import timezone
import socket 

def index(request):
    html = "<h1>Welcome</h1>"
    response = HttpResponse(html)
    response['Data-Atual'] = timezone.localtime(timezone.now())

    return response

  
# Function to display hostname and 
# IP address por cokkie
    host_name = socket.gethostname() 
    host_ip = socket.gethostbyname() 
  
def setCookie(request):
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name) 

    response = HttpResponse()
    response.set_cookie("my_name", value=host_ip)

    return response

def redirect(request):
    return HttpResponseRedirect('https://uol.com.br')