from basketapp.models import Basket


def basket(request):
    print(f'context processor basket works')
    basket = []

    if request.user.is_authenticated:
        basket = Basket.get_items(request.user).select_related()

    return {
        'basket': basket,
    }