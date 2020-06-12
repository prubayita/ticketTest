from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='qrcode'),
    # path('<int:qrcode_id>', views.listing, name='qrcode'),
    # path('search', views.search, name='search'),
]
