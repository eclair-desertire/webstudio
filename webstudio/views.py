from django.shortcuts import render
from .forms import OrderForm

def main_page(request):
    return render(request,'webstudio/main_page.html',{})

def order_new(request):
    form=OrderForm()
    return render(request,'webstudio/order_new.html',{'form':form})
# Create your views here.
