from django.urls import path
from . import views

urlpatterns=[
    path('', views.ticket, name='ticket'),
    # path('<int:listing_id>', views.listing, name='tickets'),
    path('search', views.search, name='search'),
]
