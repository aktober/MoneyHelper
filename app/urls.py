from django.urls import path
from app.api import views
from app.views import HomePage, DashboardPage, LoginView, SignUpView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('api/currencies/', views.CurrencyList.as_view()),
    path('api/currencies/<int:pk>/', views.CurrencyDetail.as_view()),
    path('api/accounts/', views.AccountCreateList.as_view()),
    path('api/account/<int:pk>/', views.AccountRUD.as_view()),

    path('api/users/', views.UserCreateListAPI.as_view()),
    path('api/user/<int:pk>/', views.AccountRUD.as_view()),

    path('api/login/', views.LoginApi.as_view()),

    path('', HomePage.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('dashboard/', login_required(DashboardPage.as_view()), name='dashboard'),
]
