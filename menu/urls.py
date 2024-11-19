from django.urls import path
from . import views

urlpatterns = [
    path('<int:table_number>/', views.menu, name='menu_with_table'),
    path('<int:table_number>/add-to-cart/<int:dish_id>/', views.add_to_cart, name='add_to_cart_with_table'),
    path('<int:table_number>/cart/', views.cart, name='cart_with_table'),
    path('<int:table_number>/checkout/', views.checkout, name='checkout_with_table'),
    path('orders/', views.orders, name='orders'),
    path('set_language/<int:table_number>/', views.set_language, name='set_language'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('menu/oplata/', views.oplata, name='oplata'),
]