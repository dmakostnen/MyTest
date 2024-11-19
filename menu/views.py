from django.shortcuts import render, get_object_or_404, redirect
from .models import Dish, Order
from .forms import OrderForm
from django.contrib.admin.models import LogEntry


from django.utils.translation import activate

def menu(request, table_number):
    dishes = Dish.objects.all()
    return render(request, 'menu/menu.html', {'dishes': dishes, 'table_number': table_number})

def add_to_cart(request, table_number, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    cart = request.session.get('cart', {})

    if str(table_number) not in cart:
        cart[str(table_number)] = []

    cart_item = next((item for item in cart[str(table_number)] if item["dish_id"] == dish_id), None)

    if cart_item:
        cart_item["quantity"] += int(request.POST.get('quantity', 1))
    else:
        cart[str(table_number)].append({
            "dish_id": dish_id,
            "dish_name": dish.name,
            "quantity": int(request.POST.get('quantity', 1)),
            "price": str(dish.price)
        })

    request.session['cart'] = cart
    return redirect('cart_with_table', table_number=table_number)

def cart(request, table_number):
    cart = request.session.get('cart', {}).get(str(table_number), [])
    total_price = sum(float(item['price']) * item['quantity'] for item in cart)
    return render(request, 'menu/cart.html', {'cart': cart, 'total_price': total_price, 'table_number': table_number})

def checkout(request, table_number):
    cart = request.session.get('cart', {}).get(str(table_number), [])
    total_price = sum(float(item['price']) * item['quantity'] for item in cart)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.table_number = table_number
            order.order_items = cart
            order.total_price = total_price
            order.save()
            del request.session['cart'][str(table_number)]
            return redirect('oplata')
    else:
        form = OrderForm(initial={'table_number': table_number, 'total_price': total_price})

    return render(request, 'menu/checkout.html', {'form': form, 'total_price': total_price, 'table_number': table_number})

def orders(request):
    orders = Order.objects.all()
    return render(request, 'menu/orders.html', {'orders': orders})


def set_language(request, table_number):

    return render(request, "menu/leng.html", {'table_number': table_number})

def clear_cart(request):
    # Очистка корзины (например, удаление всех элементов из сессии, относящихся к корзине)
    if 'cart' in request.session:
        del request.session['cart']
    return render(request,'menu/menu.html')

def oplata(request):
    return render(request, "menu/oplata.html")