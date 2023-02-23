from django.contrib import admin
from django.urls import path
from main.views import VinRetrieveApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', VinRetrieveApiView.as_view()),
]
