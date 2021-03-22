from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('accounts/register', RegisterView.as_view(), name='register'),
    path('personal/', personal),
    path('change/<int:id>/', change_image, name='image-detail'),
    path('/accounts/profile/', redirect_view)
]