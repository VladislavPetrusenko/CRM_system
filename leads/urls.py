from django.urls import path
from leads import views

urlpatterns = [
    path('', views.LeadListView.as_view(), name='leads_list'),
    path('create/', views.LeadCreateView.as_view(), name='lead_create'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='lead_detail'),
    path('<int:pk>/update/', views.LeadUpdateView.as_view(), name='lead_update'),
    path('<int:pk>/delete/', views.LeadDeleteView.as_view(), name='lead_delete')
]
