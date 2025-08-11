from django.conf import settings
def restaurant_name(request):
    return{
        'restaurant_name': getattr(settings,'RESTAURANT_NAME','Restaurant'},
        'restaurant_phone': getattr(settings,'RESTAURANT_PHONE', 'N/A'),
        }