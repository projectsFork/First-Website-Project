from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html = ""
    html += "<h1>This is a WebSite for EDGARRAW!!!</h1>"
    html += "<h3>About:</h3>"
    html += "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    return HttpResponse(html)
