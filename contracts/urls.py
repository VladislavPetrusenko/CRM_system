from django.urls import path
from .views import (
    ContractCreateView,
    ContractDeleteView,
    ContractDetailView,
    ContractListView,
    ContractUpdateView
)

urlpatterns = [
    path('', ContractListView.as_view(), name='contracts_list'),
    path('create/', ContractCreateView.as_view(), name='contract_create'),
    path('<int:pk>/', ContractDetailView.as_view(), name='contract_detail'),
    path('<int:pk>/update/', ContractUpdateView.as_view(), name='contract_update'),
    path('<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete')
]
