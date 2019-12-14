import ordersapp.views as ordersapp
from django.urls import re_path, path


app_name = "ordersapp"


url_patterns = [
    re_path(r'^S', ordersapp.OrderList.as_view(),
            name='orders_list'),
    re_path(r'^forming/complete/(?P<pk>\d+)/',
            ordersapp.order_forming_complete,
            name='order_forming_complete'),
    path('create/', ordersapp.OrderItemsCreate.as_view(),
         name='order_create'),
    path('read/<int:pk>/', ordersapp.OrderRead.as_view(),
         name='order_read')
    path('update/<int:pk>/', ordersapp.OrderItemsUpdate.as_view(),
         name='order_update')
    path('delete/<int:pk>/', ordersapp.OrderDelete.as_view(),
         name='order_delete')
]