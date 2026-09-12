from django.urls import path
from services.views import (
    ServiceCreateView,
    ServiceDeleteView,
    ServiceDetailView,
    ServiceListView,
    ServiceUpdateView
)

urlpatterns = [
    path('', ServiceListView.as_view(), name='services_list'),
    path('create/', ServiceCreateView.as_view(), name='service_create'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('<int:pk>/update', ServiceUpdateView.as_view(), name='service_update'),
    path('<int:pk>/delete', ServiceDeleteView.as_view(), name='service_delete')
]
