from django.urls import path

from .views import (
    ContactusView,
    PostsList,
)

urlpatterns = [
    path('contactus/', ContactusView.as_view()),
    path('posts/', PostsList.as_view())
]
