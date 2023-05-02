from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# views.py
def index(request):
    return render(request, 'index.html')


# def contacts(request):
#     return render(request, 'contacts.html')


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(f"'name': {name}, 'phone': {phone}, 'message': {message}")
        return render(request, 'contacts.html', {'name': name, 'phone': phone, 'message': message})
    else:
        return render(request, 'contacts.html')

def getdata(request):
    name = request.POST.get('name', '')
    phone = request.POST.get('phone', '')
    message = request.POST.get('message', '')
    print(f"'name': {name}, 'phone': {phone}, 'message': {message}")
    return HttpResponse(f"<h2>'name': {name}, 'phone': {phone}, 'message': {message}</h2>")