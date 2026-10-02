"""Представления статистики"""

from decimal import Decimal
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum
from django.views.generic import ListView
from compaigns.models import Compaign


class CompaignStatisticView(LoginRequiredMixin, ListView):
    """Страница статистики рекламных кампаний."""
    template_name = 'analytics/compaign_analytics.html'
    context_object_name = 'compaign_list'


    def get_queryset(self):
        """Выбирает кампании с посчитанными показателями одним запросом."""
        return Compaign.objects.annotate(
            leads_count=Count('leads', distinct=True),
            clients_count=Count('leads__active_client', distinct=True),
            income=Sum('leads__active_client__contract__amount')
        )


    def get_context_data(self, **kwargs):
        """Досчитывает соотношение дохода и бюджета для каждой кампании."""
        context = super().get_context_data(**kwargs)
        for compaign in self.object_list:
            compaign.income = compaign.income or Decimal('0.00')
            if compaign.budget:
                compaign.profit = round(compaign.income / compaign.budget, 2)
            else:
                compaign.profit = None
        return context
