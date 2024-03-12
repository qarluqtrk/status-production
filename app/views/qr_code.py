from django.shortcuts import redirect

from app.models.other import QRCodeURL


def review(request):
    url = QRCodeURL.objects.first()
    return redirect(url.url)
