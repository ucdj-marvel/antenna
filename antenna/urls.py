from django.urls import path

from antenna.views import (
    IndexView,
    SignUpView
)


app_name = 'antenna'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
]