from django.urls import path
from.import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('menu/', views.menu,name='menu'),
    path('contact/',views.contact,name='contact'),
    path('reservations/',views.reservations,name='reservaions'),
    path('search/', views.search_results,name='search'),
    path('feedback/', views.feedback_view,name='feedback'),
    path('feedback/success/', views. feedback_success,name='feedback_success'),
    path('api/menu/',views.menu_api,name='menu_api'),
]