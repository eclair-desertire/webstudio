from django.shortcuts import render

def main_page(request):
    return render(request,'webstudio/main_page.html',{})
# Create your views here.
