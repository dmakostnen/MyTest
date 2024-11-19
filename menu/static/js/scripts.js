// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Найти все кнопки "Добавить в корзину" и добавить обработчик события на каждую из них
    var addToCartButtons = document.querySelectorAll('.add-to-cart');

    addToCartButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            // Отменить действие по умолчанию (например, перезагрузку страницы)
            event.preventDefault();

            // Получить идентификатор блюда из атрибута data-dish-id
            var dishId = button.getAttribute('data-dish-id');

            // Получить количество товара из соответствующего поля ввода
            var quantityInput = document.getElementById('quantity-' + dishId);
            var quantity = quantityInput.value;

            // Опционально: валидация количества, например, проверка на положительное число

            // Отправить AJAX запрос на сервер для добавления товара в корзину
            addToCart(dishId, quantity);
        });
    });

    // Функция для отправки AJAX запроса на сервер
    function addToCart(dishId, quantity) {
        var url = '/add-to-cart/'; // Указать URL для добавления в корзину

        // Определить данные для отправки (можно использовать JSON)
        var data = {
            'dish_id': dishId,
            'quantity': quantity
        };

        // Отправить AJAX POST запрос
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Получить CSRF токен для защиты
            },
            body: JSON.stringify(data)
        })
        .then(function(response) {
            // Обработать ответ от сервера
            if (response.ok) {
                // Успешное добавление в корзину, выполнить необходимые действия
                console.log('Товар добавлен в корзину!');
                // Опционально: обновить интерфейс, например, показать уведомление
            } else {
                // Обработать ошибку при добавлении в корзину
                console.error('Ошибка при добавлении товара в корзину');
            }
        })
        .catch(function(error) {
            // Обработать ошибку сети или другие ошибки
            console.error('Ошибка сети:', error);
        });
    }

    // Функция для получения CSRF токена из cookie
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Найти cookie с заданным именем
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
