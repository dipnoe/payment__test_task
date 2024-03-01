from http import HTTPStatus

from django.http import JsonResponse
from django.shortcuts import render
import stripe

from config.settings import STRIPE_SECRET_KEY
from payment.models import Item

from config.settings import STRIPE_PUBLIC_KEY

stripe.api_key = STRIPE_SECRET_KEY


def get_session_id(request, item_id) -> str | JsonResponse:
    if request.method != 'GET':
        return JsonResponse({
            'status': HTTPStatus.METHOD_NOT_ALLOWED
        })

    item = Item.objects.get(pk=item_id)
    # response = stripe.PaymentIntent.create(
    #     amount=int(item.price) * 100,
    #     currency='RUB',
    #     automatic_payment_methods={
    #         "enabled": True,
    #         "allow_redirects": "never"
    #     },
    # )
    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{
            "price_data": {
                'currency': 'rub',
                'product_data': {
                    'name': item.name,
                    'description': item.description
                },
                'unit_amount_decimal': item.price * 100
            },
            "quantity": 1
        }],
        mode="payment",
    )
    return JsonResponse({
        'id': session.id,
        'status': HTTPStatus.OK
    })


def buy_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
        'STRIPE_PUBLIC_KEY': STRIPE_PUBLIC_KEY
    }
    return render(request, 'payment/item_buy.html', context=context)
