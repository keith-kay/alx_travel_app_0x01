from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add your app URLs here, for example:
    # path('', include('your_app.urls')),
]