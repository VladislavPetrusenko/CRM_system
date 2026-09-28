from django.urls import path
from .views import (
    ActiveClientDeleteView,
    ActiveClientCreateView,
    ActiveClientDetailView,
    ActiveClientListView,
    ActiveClientUpdateView
)

urlpatterns = [
    path('', ActiveClientListView.as_view(), name='clients_list'),
    path('create/', ActiveClientCreateView.as_view(), name='client_create'),
    path('<int:pk>/', ActiveClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/update/', ActiveClientUpdateView.as_view(), name='client_update'),
    path('<int:pk>/delete/', ActiveClientDeleteView.as_view(), name='client_delete')
]
