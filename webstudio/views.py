from django.shortcuts import render
from .forms import OrderForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm



def main_page(request):
    return render(request,'webstudio/main_page.html',{})

def order_new(request):

    if request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = OrderForm(request.POST)
        if form.is_valid():
            order_title = form.cleaned_data['order_title']
            order_email = form.cleaned_data['order_email']
            message = form.cleaned_data['order_info'] + form.cleaned_data['order_contacts'] + form.cleaned_data['order_date']
            send_mail(f'{order_title} от {order_email}', message,"вставь сюда нужны email", "сюда тот же самый  email")

            return redirect('main_page')
    else:
        form = OrderForm()
    return render(request,'webstudio/order_new.html',{'form':form})

# Create your views here.
