from django.urls import path
from .import views

# import views_auth for password reset
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('register/', views.registerPage, name="register"),
   path('login/',views.loginPage, name="login"),
   path('logout', views.logoutUser, name="logout"),
   path('reset_password/',auth_views.PasswordResetView.as_view(), name="reset_password"),
   path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
   path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
   path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

   path('',views.home, name="home"),
   path('newshome',views.newshome, name="newshome"),
   path('newsdetails/<str:pk>/',views.newsdetails, name="newsdetails"),
   path('addnews/',views.addnews, name="addnews"),
   path('search_results/',views.search_results, name='search_results'),
   path('profile/', views.profile, name='profile'),
]
