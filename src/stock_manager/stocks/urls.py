from django.urls import path

from stocks import views

urlpatterns = [
    path("new/", views.stock_new, name="stock_new"),
    path("<int:stock_id>/", views.stock_detail, name="stock_detail"),
    path("<int:stock_id>/edit/", views.stock_edit, name="stock_edit"),
    path("<int:stock_id>/in/", views.stock_in, name="stock_in"),
    path("<int:stock_id>/out/", views.stock_out, name="stock_out"),
    path("location/", views.shop_location, name="shop_location"),
]
