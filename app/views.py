from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'


class DashboardPage(TemplateView):
    template_name = 'dashboard.html'


class LoginPage(TemplateView):
    template_name = 'login.html'


class SignUpPage(TemplateView):
    template_name = 'signup.html'


class CurrencyPage(TemplateView):
    template_name = 'currencies.html'


class AccountPage(TemplateView):
    template_name = 'accounts.html'


class SettingsPage(TemplateView):
    template_name = 'settings.html'


class ExpensesPage(TemplateView):
    template_name = 'expenses.html'


class IncomesPage(TemplateView):
    # TODO
    pass


class CategoryPage(TemplateView):
    # TODO
    pass


class ChartPage(TemplateView):
    # TODO
    pass
