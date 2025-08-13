from django.shortcuts import render
from .forms import ContactForm
from .models import Restaurant
from .models import DatabaseError
from .models import MenuItem
def home(request):
    try:
        restaurant= Restaurant.objects.get(pk=1)
        context ={
            'restaurant_name': restaurant.name,
            'restaurant_phone': restaurant.phone_number,
            }
            except Restaurant.DoesNotExist:
                context={
                    'restaurant_name': 'My Awesome Restaurant',
                    'restaurant_phone': 'N/A',
                }
def menu(request):
    try:
        menu_items= MenuItem.objects.all()
        context={
            'menu_items': menu_items,
            'message': None,
        }
    except DatabaseError:
        menu_items=[]
        context={
            'menu_items': menu_items,
            'message': 'WE ARE CURRENTLY EXPERIENCING TECHNICAL DIFFICULTIES. PLEASE STANDBY.'
        }
        return render(request,'restaurant_management/menu.html',context)
    return render(request,'restaurant_management/home.html',context)
    def about(request):
        return render(request,'restaurant_management/about.html')
        def contact(request):
            return render(request,'restaurant_management/contact.html')
            def reservations(request):
                return render(request,'restaurant_management/reservations.html')
                def search_results(request):
                    query= request.GET.get('q')
                    context={'query': query}
                    return render(request,'restaurant_management/search_results.html',context)
           def conatact_form_view(request):
            if request.method == 'POST':
                form = ContactForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('homepage')
                    else:
                        form=ContactForm()
                        return render(request,'homepage.html',{'form': form})
                        