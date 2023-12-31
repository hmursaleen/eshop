from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('signup/', views.signup, name='signup'),
	path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('myaccount/', views.myaccount, name='myaccount'),
	path('mystore/', views.mystore, name='mystore'),
	path('mystore/order-detail/<int:pk>/', views.mystore_order_detail, name='mystore_order_detail'),
	path('mystore/add-product', views.add_product, name='add_product'),
	path('mystore/edit-product/<int:pk>/', views.edit_product, name='edit_product'),
	path('mystore/delete-product/<int:pk>/', views.delete_product, name='delete_product'),
	path('vendor/<int:pk>/', views.vendor_detail, name='vendor_detail'),
]