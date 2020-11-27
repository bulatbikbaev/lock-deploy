from django.urls import path
from .views import MasterKeyList, MasterKeyDetail


urlpatterns = [
    path('master/<int:pk>/', MasterKeyDetail.as_view()),
    path('master/', MasterKeyList.as_view())
]
