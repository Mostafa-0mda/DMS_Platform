from  django.urls import path, include
from .views import api_home
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('auth/', obtain_auth_token),
  path('home/', api_home),
  path('products/', include('products.urls'))
]