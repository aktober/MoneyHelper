from django.urls import path, include
from app.api import views as api_views
from app.api.views import CurrencyViewSet, AccountViewSet, UserViewSet
from app.views import HomePage, DashboardPage, LoginPage, SignUpPage
from app import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet, basename='Currency')
router.register(r'accounts', AccountViewSet, basename='Account')
router.register(r'users', UserViewSet, basename='User')

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpPage.as_view(), name='signup'),
    path('dashboard/', login_required(DashboardPage.as_view()), name='dashboard'),

    # API
    path('api/', include(router.urls)),
    path('api/login/', api_views.LoginApi.as_view()),

    path('currencies/', views.CurrencyPage.as_view(), name='currencies'),
    path('accounts/', views.AccountPage.as_view(), name='accounts'),
    path('expenses/', views.ExpensesPage.as_view(), name='expenses'),
    path('incomes/', views.IncomesPage.as_view(), name='incomes'),
    path('chart/', views.ChartPage.as_view(), name='chart'),
    path('categories/', views.CategoryPage.as_view(), name='categories'),
    path('settings/', views.SettingsPage.as_view(), name='settings'),
]
