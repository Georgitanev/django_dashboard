from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("google_analytics/", include("google_analytics.urls")),
    path("", RedirectView.as_view(url="/google_analytics/", permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
