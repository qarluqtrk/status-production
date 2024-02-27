from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from app.forms import ReviewModelForm, BookingModelForm
from app.models.other import Review, Around
from app.models.room import RoomCategory, Room, RoomAmenity


def rooms_view(request):
    if request.method == "POST":
        form = BookingModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = BookingModelForm()
    categories = RoomCategory.objects.all()
    rooms = Room.objects.all()
    paginator = Paginator(rooms, per_page=6)
    page_number = request.GET.get('page')
    rooms_list = paginator.get_page(page_number)
    reviews = Review.objects.filter(is_active=True, main=True).order_by('created_at').all()

    return render(request=request, template_name='app/rooms.html',
                  context={'categories': categories,
                           'rooms': rooms_list,
                           'reviews': reviews,
                           'form': form})


def room_details(request, room_id):
    if request.method == "POST":
        form_type = request.POST.get('form_type')
        if form_type == 'form1':
            form = ReviewModelForm(data=request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.room = get_object_or_404(klass=Room, id=room_id)
                review.save()
                return redirect('room_details', room_id)
        elif form_type == 'form2':
            form = BookingModelForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('room_details', room_id)

        elif form_type == 'form3':
            form = BookingModelForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('room_details', room_id)

    form = BookingModelForm()

    # if request.method == 'POST':
    #     form = ReviewModelForm(data=request.POST)
    #     if form.is_valid():
    #         review = form.save(commit=False)
    #         review.room = get_object_or_404(klass=Room, id=room_id)
    #         review.save()
    #         return redirect('room_details', room_id)
    # form = ReviewModelForm()
    room = Room.objects.filter(id=room_id).first()
    arounds = Around.objects.all()
    rooms = Room.objects.order_by("-id").all()[:3]
    amenities = RoomAmenity.objects.filter(room=room).all()
    reviews = Review.objects.filter(room_id=room_id).order_by('created_at').all()[:3]
    return render(request=request, template_name='app/room_details.html',
                  context={'room': room,
                           'arounds': arounds,
                           'rooms': rooms,
                           'amenities': amenities,
                           'form': form,
                           'reviews': reviews})
