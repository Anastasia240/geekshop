from django.shortcuts import render

# Create your views here.

links_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'products_home', 'name': 'дом'},
    {'href': 'products_office', 'name': 'офис'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'}

]


def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')


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

def login(request):
    return HttpResnonse('Ok!')
