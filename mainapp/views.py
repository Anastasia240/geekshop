from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product
import json
import os

# Create your views here.

links_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'products_home', 'name': 'дом'},
    {'href': 'products_office', 'name': 'офис'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'}

]

menu = [
    {'href': 'main', 'name': 'главная'},
    {'href': 'product:index', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'}
]

module_dir = os.path.dirname(__file__)


def main(request):
    content = {'menu': menu}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)
    # file_path = os.path.join(module_dir, 'json/products.json')
    # products = json.load(open(file_path))

    title = 'Продукты'

    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authentcated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'Все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'products': products,
            'category': category,
            'menu': menu,
            'basket': basket
        }
        return render(request, 'mainapp/products.html', content)

    same_products = Product.objects.all()[:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'menu': menu

    }
    return render(request, 'mainapp/products_list.html', content)

def contact(request):
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-123-45-6789',
            'email': 'master@master.ru',
            'address': 'Москва, ул. Тверская, 15,'
        },
        {
            'city': 'Ростов-на-Дону',
            'phone': '+7-987-65-4321',
            'email': 'master@master.ru',
            'address': 'Ростов-на-Дону, ул Горького, 100',
        },
        {
            'city': 'Иркутск',
            'phone': '+7-112-445-6677',
            'email': 'master@master.ru',
            'address': 'Иркутск, бульвар Гагарина, 21',
        }
    ]

    content = {
        'page_title': 'контакты',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', content)


def context(request):
    content = {
        'title': 'магазин',
        'header': 'Добро пожаловать на сайт',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Стулья', 'price': 4000},
            {'name': 'Диван', 'price': 5000},
            {'name': 'Кровати', 'price': 10000},
        ]
    }
    return render(request, 'mainapp/test_context.html', content)


def main(reguest):
    title = 'главная'

    products = Product.objects.all()[:3]

    content = {
        'title': title,
        'products': products,
        'contact': contact,

    }

    return render(reguest, 'mainapp/index.html', content)


def login():
    return
