from django.shortcuts import render


def rooms_view(request):
    return render(request=request, template_name='app/rooms.html')
