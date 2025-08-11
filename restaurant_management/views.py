from django.shortcuts import render
def home(request):
    return render(request,'restaurant_management/home.html',context)
    def about(request):
        return render(request,'restaurant_management/about.html')