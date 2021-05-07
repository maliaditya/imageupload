from django.urls import path

from . import views

urlpatterns = [
    path('image/', views.ImageList.as_view()),
    path('image/<int:pk>', views.ImageDetail.as_view()),
]
