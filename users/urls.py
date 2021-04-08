from django.urls import path
from .views import register, login_user, logout_user, AllUsers


urlpatterns = [
    path('', AllUsers.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]