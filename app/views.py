from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'


class DashboardPage(TemplateView):
    template_name = 'dashboard.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class SignUpView(TemplateView):
    template_name = 'signup.html'
