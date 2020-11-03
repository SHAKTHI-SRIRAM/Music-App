from django.urls import path, re_path
from .views import ApiView

urlpatterns = [
    re_path('', ApiView.as_view(), name='api_view')
]