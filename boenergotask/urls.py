from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # apps urls files include
    path('home/', include('home.urls')),
    path('quadraticequation/', include('quadraticequation.urls')),
    path('hundreditems/', include('hundreditems.urls')),

    # index redirection
    path('', RedirectView.as_view(url='/home/', permanent=True)),
]

# Используйте static() чтобы добавить соотношения для статических файлов
# Только на период разработки

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
