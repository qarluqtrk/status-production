from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app.views.other.main import set_language

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
    path("set_language/<str:language>", set_language, name="set-language"),

    path('', include('app.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
