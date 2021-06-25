from django.shortcuts import render
from .forms import OrderForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect




def main_page(request):
    return render(request,'webstudio/main_page.html',{})

def order_new(request):

    if request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = OrderForm(request.POST)
        if form.is_valid():
            order_name = form.cleaned_data['order_name']
            order_email = form.cleaned_data['order_email']
            order_info = form.cleaned_data['order_info']
            send_mail(f'{order_name} от {order_email}', order_info,"вставь сюда нужны email", "сюда тот же самый  email")

            return redirect('main_page')
    else:
        form = OrderForm()
    return render(request,'webstudio/order_new.html',{'form':form})

# Create your views here.
