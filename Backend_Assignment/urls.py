
from django.contrib import admin
from django.urls import path
from app.views import MessageAPIView,LikeAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',MessageAPIView.as_view()),
    path('like/',LikeAPIView.as_view())
]
