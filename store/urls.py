from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('<slug:slug>', views.product_detail_page,
         name='product_detail_page'),
    path('category/<slug:category_slug>',
         views.category_list,  name="category_list")

]
