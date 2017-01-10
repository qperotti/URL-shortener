
from django.conf.urls import url
from django.contrib import admin

from analytics.api.views import ClickEventAPIView

urlpatterns = [
    url(r'^(?P<id>\d+)/', ClickEventAPIView.as_view(), name='list'),
]
