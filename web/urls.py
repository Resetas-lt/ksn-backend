from django.urls import path

from .views import (
    ContactusView,
    PostsList,
    PostDetails,
    ContactList,
)

urlpatterns = [
    path('contactus/', ContactusView.as_view()),
    path('posts/', PostsList.as_view()),
    path('posts/<slug:slug>/', PostDetails.as_view()),
    path('contacts/', ContactList.as_view()),
]
