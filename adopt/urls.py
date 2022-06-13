from django.urls import path
from .views import AdoptList

urlpatterns = [
    path('', AdoptList.as_view())
]
