import src.dataset.views as dataset
from django.urls import path

app_name = 'dataset'

urlpatterns = [
    path('<str:fio>/', dataset.client_view, name='client'),
    path('company/<int:company_id>/', dataset.approved_list,)
]