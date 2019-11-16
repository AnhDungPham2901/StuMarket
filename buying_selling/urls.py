from django.urls import path

from buying_selling.views import SellView,DangBanView,BuyView,DangMuaView
from buying_selling import views
urlpatterns = [
    # path('buy/', BuyView.as_view(), name='buy'),
    path('buy/',views.BuyView,name='buy'),
    path('dangmua/',DangMuaView.as_view(),name='dangmua'),
    # path('sell/', SellView.as_view(), name='sell'),
    path('sell/',views.SellView,name='sell'),
    path('dangban/',DangBanView.as_view(),name='dangban'),
    # path('new/',views.Load_Product_Ban),
]
