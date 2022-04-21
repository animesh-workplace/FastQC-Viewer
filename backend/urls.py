from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('fastqc/admin/', admin.site.urls),
    path('fastqc/api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('fastqc/api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('fastqc/api/v1/', include('users.urls')),
    path('fastqc/api/', include('fastqc.urls'))
]
