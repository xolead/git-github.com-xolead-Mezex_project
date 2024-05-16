from django.contrib import admin
from django.urls import path, include
from invest import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('offers/', views.offers, name='offers'),
    path('create/', views.create, name='create'),
    path('view_files/', views.view_files, name='view_files'),
    path('delete/<int:id>/<int:idInv>', views.HomeDelete, name='delete' ),
    path('create/<int:id>', views.CreateDelete, name='CreateDelete'),
    path('newpred/<int:idAns>', views.NewPred, name='NewPred'),
    path('newrequest', views.NewRequest, name='NewRequest'),
]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += [
    # Другие URL-маршруты...
    path('logout/', views.logout_view, name='logout'),
]
