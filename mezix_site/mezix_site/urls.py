from django.contrib import admin
from django.urls import path, include
from invest import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('offers/', views.offers, name='offers'),
    path('create/', views.create, name='create')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += [
    # Другие URL-маршруты...
    path('logout/', views.logout_view, name='logout'),
]
