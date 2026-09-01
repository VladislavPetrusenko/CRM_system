from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from services.models import Service


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services_count"] = Service.objects.count()
        return context
    