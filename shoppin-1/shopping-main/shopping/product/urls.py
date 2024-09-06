from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name = "index"),
    path("reg",views.signup, name="signup"),
    path("product",views.product, name="product"),
    path("cart",views.view_cart, name="cart"),
    path("delete/<int:id>",views.delete, name="delete"),
    path("add_to_cart/<int:id>",views.add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<int:id>" ,views.remove_from_cart, name="remove_from_cart" ),
    path("checkOut",views.check_out,name="checkout")
]