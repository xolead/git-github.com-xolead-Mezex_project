from django.contrib import admin
from django.urls import path, include
from invest import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += [
    # Другие URL-маршруты...
    path('logout/', views.logout_view, name='logout'),
]
