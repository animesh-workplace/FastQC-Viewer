from django.urls import path
from .views import CustomerRegView, HomeView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404, handler500

urlpatterns = [
                  path('', CustomerRegView.as_view(), name="login"),
                  path('accounts/login/', CustomerRegView.as_view()),
                  path('profile/', HomeView.as_view(), name="home"),
                  path('profile/<str:pt>', HomeView.as_view(), name="projectdetail"),
                  path('profile/<str:dt>/<str:pt>/<str:data>/<str:data1>', views.show_data, name="show"),
                  path('data/', views.data_store, name="main"),
                  path('profile/<str:pro>/<str:ptt>/<str:st>/<str:fs>/<str:smmp>', views.multiqc, name="multi"),
                  path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'api.views.handler404'

handler500 = 'api.views.handler500'
