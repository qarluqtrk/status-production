from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from app.forms import BookingModelForm
from app.models.blog import Blog
from app.models.other import Review
from app.models.restaurant import RestaurantResult, Menu, RestaurantGallery, MenuCategory


def restaurant_view(request):
    if request.method == "POST":
        form = BookingModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = BookingModelForm()
    restaurant_results = RestaurantResult.objects.all()
    products = Menu.objects.all()
    blogs = Blog.objects.order_by("-created_at").all()[:3]
    restaurant_galleries = RestaurantGallery.objects.all()
    return render(request=request, template_name='app/restaurant.html',
                  context={'restaurant_results': restaurant_results,
                           'products': products,
                           'restaurant_galleries': restaurant_galleries,
                           "blogs": blogs,
                           'form': form})


def menu_view(request):
    if request.method == "POST":
        form = BookingModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = BookingModelForm()
    reviews = Review.objects.filter(is_active=True, main=True).order_by('created_at').all()
    categories = MenuCategory.objects.all()
    products = Menu.objects.all()
    paginator = Paginator(products, per_page=6)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    return render(request=request, template_name='app/menu.html',
                  context={'categories': categories,
                           'products': product_list,
                           "reviews": reviews,
                           "form": form
                           })
