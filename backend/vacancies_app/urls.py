from django.urls import path, include
from .api.routes import router

urlpatterns = [
    path('', include(router.urls)),
]
