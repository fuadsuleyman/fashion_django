from django.shortcuts import render, redirect
# from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from account.models import *
from order.models import *
from .filters import ProductFilter
from product.models import (
    Product,
    Product_sizes_rel
)

# Create your views here.


def category_page(request):
    products = Product.objects.all()

    myfilter = ProductFilter(request.GET, queryset=products)

    products = myfilter.qs
    
    return render(request, 'product/category_page.html', {'products': products, 'myfilter': myfilter})


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'product/product.html'
#     context_object_name = 'product'

#     def get_context_data(self, **kwargs):
    
#         context = super().get_context_data(**kwargs)
#         product = self.object
#         size = self.request.GET.get('size')
        
#         if size:
#             filter_size = Product_sizes_rel.objects.filter(product_sizes__size = size).filter(product = self.object)
#             context['in_stock'] = filter_size.first().in_stock
#             context['size'] = size
#         # asagida size='s' yazdimki default olaraq sehife acilanda s size-inda active klasi olasun
#         else:
#             filter_size = Product_sizes_rel.objects.filter(product_sizes__size = 's').filter(product = self.object)
#             context['in_stock'] = filter_size.first().in_stock
#             context['size'] = 's'

#         return context

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    size = request.GET.get('size')

    if size:
        filter_size = Product_sizes_rel.objects.filter(product_sizes__size = size).filter(product = product)
        context = {'product':product, 'in_stock':filter_size.first().in_stock, 'size':size}
    else:
        filter_size = Product_sizes_rel.objects.filter(product_sizes__size = 's').filter(product = product)
        context = {'product':product, 'in_stock':filter_size.first().in_stock, 'size':'s'}
        
    if request.method == 'POST':
        product = Product.objects.get(slug=slug)
        #Get user account information
        try:
            customer = request.user.customer	
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity=request.POST['quantity']
        orderItem.save()

        return redirect('cart')

    return render(request, 'product/product.html', context)