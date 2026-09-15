from django.urls import path
from .views import CompaignCreateView, CompaignDeleteView, CompaignDetailView, CompaignListView, CompaignUpdateView


urlpatterns = [
    path('', CompaignListView.as_view(), name='compaigns_list'),
    path('create/', CompaignCreateView.as_view(), name='compaign_create'),
    path('<int:pk>/', CompaignDetailView.as_view(), name='compaign_detail'),
    path('<int:pk>/update/', CompaignUpdateView.as_view(), name='compaign_update'),
    path('<int:pk>/delete/', CompaignDeleteView.as_view(), name='compaign_delete')
]
