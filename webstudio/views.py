from django.shortcuts import render
from .forms import OrderForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect




def main_page(request):
    if request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = OrderForm(request.POST)
        if form.is_valid():
            order_title = form.cleaned_data['order_title']
            order_email = form.cleaned_data['order_email']
            info = form.cleaned_data['order_info']
            info2 = form.cleaned_data['order_number']
            info3 = form.cleaned_data['order_content']


            info_end = "Имя: " + order_title+ " Что разработать?: " +  info + " Номер: " + info2 + " Описаине: " +  info3


            
            send_mail(
                        order_email,
                        info_end,
                        'zinovievakinov1234@gmail.com',

                        ['zinovievakinov1234@gmail.com'],

                        fail_silently=True,
                    )

            return redirect('main_page')
    else:

        form = OrderForm()
    return render(request,'webstudio/index.html',{'form':form})


