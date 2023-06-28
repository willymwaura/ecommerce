from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('store', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('product/<int:id>/', views.product, name='product'),
    path('lipa/',views.lipa,name='lipa'),
    path('mpesa',views.lipa_na_mpesa,name="mpesa"),
    path('',views.homepage,name='homepage'),
    path('visa',views.visa,name='visa')
    

]