from django.urls import path
from payment.apps import PaymentConfig

from payment.views import buy_item, get_session_id

app_name = PaymentConfig.name

urlpatterns = [
    path('buy/<int:item_id>/', buy_item, name='buy_item'),
    path('get/<int:item_id>/', get_session_id, name='get_session_id'),
]
