from django.urls import path

from .views import index

urlpatterns = [
    path('index/', index, {'name': 'Главная страница'}, name='index'),
    path('store/', index, {'name': 'Магазин'}, name='store'),
    path('store/contacts', index, {'name': 'Контакты'}, name='store_contacts'),
    path('store/contacts/about', index, {'name': 'О магазине'}, name='store_about'),
    path('cargo/', index, {'name': 'Доставка'}, name='cargo'),
    path('basket/', index, {'name': 'Корзина'}, name='basket'),
    path('basket/order', index, {'name': 'Сделать заказ'}, name='basket_order'),
    path('prices/', index, {'name': 'Цены'}, name='prices'),
    path('goods/', index, {'name': 'Все товары'}, name='goods'),
    path('goods/accessories/begs', index, {'name': 'Сумки'}, name='accessories_begs'),
    path('goods/accessories/hats', index, {'name': 'Головные уборы'}, name='accessories_hats'),
    path('goods/accessories/', index, {'name': 'Аксессуары'}, name='accessories'),
    path('goods/shoes/', index, {'name': 'Обувь'}, name='goods_shoes'),
    path('goods/shoes/sport/', index, {'name': 'Спортивная обувь'}, name='goods_sport_shoes'),
    path('goods/shoes/classic/', index, {'name': 'Туфли'}, name='goods_classic_shoes'),
    path('goods/cloth/', index, {'name': 'Одежда'}, name='goods_cloth'),
    path('goods/cloth/shirt/', index, {'name': 'Рубашки'}, name='goods_cloth_shirt'),
    path('goods/cloth/trousers/', index, {'name': 'Брюки'}, name='goods_cloth_trousers'),

]
