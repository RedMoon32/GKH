import src.dataset.views as dataset
from django.urls import path

app_name = 'dataset'

urlpatterns = [
    path('<str:fio>/', dataset.client_view, name='client'),
    path('company/<str:company_name>/', dataset.approved_list,)
]