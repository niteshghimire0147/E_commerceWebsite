from django.http import request
import product
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View,TemplateView
from carts.models import Item, OrderItem
from .models import top_slider
from carts.models import Category,Brand

images_choices = [
    ('carousel_image', 'carousel_image'),
    ('collection_image', 'collection_image'),
    ('discount_banner', 'discount_banner'),
    ('discount_time_banner', 'discount_time_banner'),
]

image_choice = {
    ('hot_item', 'hot_item'),
    ('best_sale', 'best_sale'),
    ('top_view', 'top_view'),
    ('on_sale', 'on_sale'),
}


def home(request):
    context={}
    try:
        for (chi,hi) in image_choice:
            filter_item = Item.objects.filter(choice=chi)
            context[chi]=filter_item
            print(chi)
        else:
            filter_item = Item.objects.all()
    except:
        filter_item = Item.objects.all()

    try:
        for (ch,ki) in images_choices:
            filter_image = top_slider.objects.filter(name=ch)
            context[ch]=filter_image 
        else:
            filter_image = top_slider.objects.all()
    except:
        filter_image = top_slider.objects.all()


    # context['carousel_image']=top_slider.objects.filter(name="carousel_image")

    if 1:
        if 'brand' in request.GET  and 'search' not in request.GET:
            brand = Brand.objects.get(id=request.GET['brand'])
            item = Item.objects.filter(brand=brand).order_by('-title')
        

        elif 'category' in request.GET  and 'search' not in request.GET:
            category = Category.objects.get(id=request.GET['category'])
            item = Item.objects.filter(brand=category).order_by('-title')

        elif 'search' in request.GET  and 'brand' not in request.GET:
            search = request.GET['search']
            item = Item.objects.filter(title__icontains = search)
        else:
            item = Item.objects.all()
        brand = Brand.objects.all()
        category = Category.objects.all()
    else:
        brand = Brand.objects.all()
        item = Item.objects.all()
        category = Category.objects.all()
    brand = Brand.objects.all()
    context["brand"]=brand
    context["category"]=category
    context['item']=item
    orderitem = OrderItem.objects.all()
    context["order"]=orderitem
    return render(request, 'index.html', context)

def contact(request):

    return render(request, 'blog-single-sidebar.html')

class ProductView(TemplateView):


    template_name = "shop-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Item'] = Item.objects.all()
        context['slider'] = top_slider.objects.all()
        context['order'] = OrderItem.objects.all()
        return context


def products_list(request):
    if 'search' in request.GET:
        search = request.GET['search']
        item = Item.objects.filter(title__icontains = search)
    else:
        item = Item.objects.all()
    context = {
        'item': item,
    }
    return render(request, "shop-list.html", context)