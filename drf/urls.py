from django.contrib import admin
from django.db import router
from django.urls import path,include
from app import views
from rest_framework.routers import DefaultRouter


#creating router obj
router=DefaultRouter()

#registering
# router.register('product',views.PetroleumProductView, basename='product')
# router.register('country',views.CountryView, basename='country')
# router.register('detail',views.DetailView, basename='detail'),
router.register('sale',views.ProductSaleView, basename='sale'),
# router.register('country-sale',views.SaleHignLowView, basename='country-sale')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('create/', views.create, name='create'),
    path('',include(router.urls)),
    path('country-create/', views.CountryCreateView.as_view()),
    path('product-create/', views.ProductCreateView.as_view()),
    path('year-create/', views.YearCreateView.as_view()),
    path('detail-create/', views.DetailCreateView.as_view()),
]