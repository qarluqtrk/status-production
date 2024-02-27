from app.models import Gallery, MainSocial


def gallery_footer(request):
    galleries = Gallery.objects.all()[:6]
    if galleries is None:
        galleries = None
    return {"galleries": galleries}


def main_social(request):
    main_socials = MainSocial.objects.all()
    if main_socials is None:
        main_socials = None
    return {"main_socials": main_socials}
