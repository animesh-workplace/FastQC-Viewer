from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls'))
]

handler404 = 'api.views.handler404'

handler500 = 'api.views.handler500'
