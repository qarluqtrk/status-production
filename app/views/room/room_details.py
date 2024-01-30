from django.shortcuts import render


def room_details(request):
    return render(request=request, template_name='app/room_details.html')
