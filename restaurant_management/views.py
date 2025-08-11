from django.shortcuts import render
from .models import Restaurant
def home(request):
    try:
        restaurant= Restaurant.objects.get(pk=1)
        context ={
            'restaurant_name': restaurant.name,
            'restaurant_phone': restaurant.phone_number,
            }
            except Restaurant.DoesNotExist:
                context={
                    'restaurant_name': 'Default Restaurant Name',
                    'restaurant_phone': 'N/A',
                }
    return render(request,'restaurant_management/home.html',context)
    def about(request):
        return render(request,'restaurant_management/about.html')
        def contact(request):
            return render(request,'restaurant_management/contact.html')