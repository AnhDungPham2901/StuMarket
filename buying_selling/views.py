from django.shortcuts import render
from django.views.generic import ListView,CreateView
from buying_selling.models import DangBan,DangMua
from django.urls import reverse_lazy # new for post form
from .forms import DangBan_Form,DangMua_Form # new for post form
# Create your views here.

# class BuyView(ListView):
#     model = DangMua
#     template_name = 'buy.html'

def BuyView(request):
    if 'q' in request.POST and request.POST['q']:
        q = request.POST['q']
        selling_products = DangBan.objects.filter(product_name__icontains=q,status=1).order_by('-created_on')
    else:
        selling_products = DangBan.objects.filter(status=1).order_by('-created_on')
    template = 'buy.html'
    return render(request,template,{'selling_products':selling_products})

class DangMuaView(CreateView):
    model = DangMua
    form_class = DangMua_Form
    template_name = 'form_dangmua.html'
    success_url = reverse_lazy('buy')



# class SellView (ListView):
#     model = DangBan
#     template_name = 'sell.html'
def SellView(request):
    if 'q' in request.POST and request.POST['q']:
        q = request.POST['q']
        buying_products = DangMua.objects.filter(product_name__icontains=q,status=1).order_by('-created_on')
    else: 
        buying_products = DangMua.objects.filter(status=1).order_by('-created_on')
    template = 'sell.html'
    return render(request,template,{'buying_products':buying_products})

 
class DangBanView(CreateView):
    model = DangBan
    form_class = DangBan_Form
    template_name = 'form_dangban.html'
    success_url = reverse_lazy('sell')



     

    