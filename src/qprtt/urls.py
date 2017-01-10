
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from shortener.views import HomeView, RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[0-9A-Za-z]{4})/', RedirectView.as_view(), name='short_url'),
    url(r'^api/analytics/', include('analytics.api.urls', namespace='analytics-api')),
]

if settings.DEBUG:
	urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))