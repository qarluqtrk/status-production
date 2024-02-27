from django.core.paginator import Paginator
from django.shortcuts import render

from app.models import MenuCategory, Menu, RestaurantResult, RestaurantGallery, Review


def restaurant_view(request):
    restaurant_results = RestaurantResult.objects.all()
    products = Menu.objects.all()
    restaurant_galleries = RestaurantGallery.objects.all()
    return render(request=request, template_name='app/restaurant.html',
                  context={'restaurant_results': restaurant_results,
                           'products': products,
                           'restaurant_galleries': restaurant_galleries})


def menu_view(request):
    reviews = Review.objects.filter(is_active=True, main=True).order_by('created_at').all()
    categories = MenuCategory.objects.all()
    products = Menu.objects.all()
    paginator = Paginator(products, per_page=6)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    return render(request=request, template_name='app/menu.html',
                  context={'categories': categories,
                           'products': product_list,
                           "reviews":reviews
                           })
