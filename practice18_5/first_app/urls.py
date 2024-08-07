
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home ,name="homepage"),
    path('home/signup/',views.signup,name="signup"),
    path('home/login/',views.user_login ,name="user_login"),
    path('home/logout/',views.user_logout ,name="user_logout"),
    path('home/profile/',views.profile ,name="profile"),
    path('changePassword/',views.pass_change,name="pass_change"),
    path('update/',views.update_user,name="update_user"),
]