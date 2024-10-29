from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('telauth/', include('custom_auth.urls')),
    path('', include('game.urls'))
]
