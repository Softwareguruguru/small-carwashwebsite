from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('pay',views.pay,name='pay'),
    path('contacts',views.contacts,name='contacts'),
    
    path('export_csv',views.export_csv, name="export_csv"),
    path('payment_csv',views.payment_csv, name="payment_csv"),
    
    path('events',views.events, name="events"),
]
