from django.urls import path, include

from antenna.views import (
    IndexView,
)


app_name = 'antenna'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]