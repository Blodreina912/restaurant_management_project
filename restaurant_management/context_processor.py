from django.conf import settings
def restaurant_name(request):
    return{
        'restaurant_name': getattr(settings,'RESTAURANT_NAME','Restaurant'},
        'restaurant_phone': getattr(settings,'RESTAURANT_PHONE', 'N/A'),
        'restaurant_hours': getattr(settings,'RESTAURANT_HOURS', 'N/A'),
        }
def cart_total(request):
    total_items = 0
    if request.user.is_authenticated:
        total_items= CartItem.objects.filter(user=request.user).aggregate(total=Sum('quantity')['total'] or 0)
        else:
            cart=request.session.get('cart',{})
            total_items= sum(cart.values()) if cart else 0
    cart= request.session.get('cart',{})
    total_items= sum(item.get('quantity',0)for item in cart.values())
    return {'cart_total_items': total_items}