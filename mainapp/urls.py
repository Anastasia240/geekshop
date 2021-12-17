from django.urls import path, re_path
import mainapp.views as mainapp

app_name = "mainapp"


urlpatterns = [
    path('', mainapp.products, name="index"),
    path('category/<int:pk>/', mainapp.products, name="category"),
    path('products/', mainapp.products, name='products'),
    re_path(r'^product/(?P<pk>\d+)/$', mainapp.products, name='products'),
    path('contact/', mainapp.contact, name='contact'),
]
